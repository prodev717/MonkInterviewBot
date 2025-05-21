# Monk Interview Bot (Speech to Speech)

An AI-powered interactive Monk interview agent with **speech-to-text** and **text-to-speech** capabilities. Users can upload their resumes and get interviewed for a specified role in a realistic conversational style. Each user session is personalized with unique chat history linked to their email.

---

## Features

* **Speech-to-text:** Speak your answers directly to the bot.
* **Text-to-speech:** Bot reads questions and responses aloud.
* **Resume upload:** Upload your resume to guide interview questions.
* **Role-based interviews:** Tailored questions based on the applied role.
* **Unique user sessions:** Chat history stored separately for each user (by email).
* **Interactive web UI:** Responsive and easy-to-use frontend.
* **FastAPI backend:** Modern Python backend with LangChain + Google Gemini LLM integration.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/prodev717/MonkInterviewBot.git
cd MonkInterviewBot
```

2. Install dependencies:

```bash
uv sync
```

3. Create a `.env` file in the root directory and add your Google Gemini API key and other environment variables:

```
GOOGLE_API_KEY=your_google_api_key_here
```

4. Run the FastAPI server:

```bash
uv run uvicorn main:app
```

5. Open your browser and visit:

```
http://localhost:8000
```

---

## Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/)
* [LangChain](https://langchain.com/)
* Google Gemini AI (via `langchain_google_genai` SDK)
* JavaScript Web Speech API (SpeechRecognition & SpeechSynthesis)
* HTML/CSS for frontend UI
* uv python package manager
---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check issues or open a pull request.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---