from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Dict
from PyPDF2 import PdfReader

load_dotenv()

user_histories: Dict[str, list] = {}
user_resumes: Dict[str, str] = {}

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an HR. You're conducting a short interview for the role of {role}. Refer to the resume and chat history. Ask questions like a real HR and decide based on answers. one question at a time. begin with introduce your self"),
    ("human", "{chat_history}\nResume:\n{resume}\nAnswer: {answer}")
])

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chain = chat_template | llm

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")


def extract_text_from_pdf(file: UploadFile):
    reader = PdfReader(file.file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])


@app.post("/start")
async def start_interview(email: str = Form(...), role: str = Form(...), resume: UploadFile = File(...)):
    resume_text = extract_text_from_pdf(resume)
    user_histories[email] = []  # Start fresh
    user_resumes[email] = resume_text
    return {"message": f"Interview started for {email} - {role}"}


class InterviewResponse(BaseModel):
    answer: str
    role: str
    user_id: str


@app.post("/interview")
def interview(response: InterviewResponse):
    history = user_histories.get(response.user_id, [])
    resume = user_resumes.get(response.user_id, "No resume provided.")

    chat_history_text = "\n".join([f"Human: {msg['human']}\nAI: {msg['ai']}" for msg in history])

    result = chain.invoke({
        "role": response.role,
        "chat_history": chat_history_text,
        "resume": resume,
        "answer": response.answer
    })
    history.append({"human": response.answer, "ai": result.content})
    user_histories[response.user_id] = history

    return {"result": result.content}
