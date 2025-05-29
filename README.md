# 🚀 LangGraph Angular Agent for Web Form Automation

This project is the result of a focused, one-day sprint to build a fully functional AI agent platform that integrates data extraction, classification, and automated web form submission — all wrapped in a clean Angular frontend and powered by LangGraph orchestration.

It's far from a toy project. This was built with grit, care, and a lot of late-night debugging.

---

## 🧠 Project Overview

This LangGraph-based AI agent pulls data from:
- 🌐 [API Ninja](https://api-ninjas.com/) — for zip code, location, and demographics
- 🧠 Ollama + Mistral — for NAICS classification and fallback zip/census inference
- 🐘 PostgreSQL — for persistent storage
- 🧪 Selenium — to simulate form submission

And it orchestrates everything through LangGraph to simulate an intelligent business registration bot.

---

## 📂 Folder Structure

```
langgraph-agent/
├── backend/
│   ├── main.py
│   ├── main_api.py
│   ├── models.py
│   ├── tools/
│   │   ├── api_ninja.py
│   │   ├── naics_classifier.py
│   │   └── form_filler.py
│   └── ...
├── frontend/
│   └── langgraph-dashboard/
│       ├── src/
│       │   ├── app/
│       │   │   ├── components/
│       │   │   │   └── form-runner/
│       │   │   └── services/
│       └── ...
└── ...
```

---

## ⚙️ Setup & Run

### Backend (FastAPI)

1. Create `.env` file in `backend/`:
    ```
    API_NINJA_KEY=your_api_ninja_key
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the backend:
    ```bash
    uvicorn main_api:app --reload
    ```

4. Access the API and docs:
    - [http://localhost:8000](http://localhost:8000)
    - [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Frontend (Angular)

1. Navigate to frontend directory:
    ```bash
    cd frontend/langgraph-dashboard
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the app:
    ```bash
    ng serve
    ```

4. Visit the dashboard at:
    [http://localhost:4200](http://localhost:4200)

---

## ✅ Prerequisites

- Python 3.10+
- Node.js 18+
- Angular CLI
- PostgreSQL running locally (or via Docker)
- Ollama installed (Mistral model required)
- Valid API Ninja key in `.env`

---

## 🛠 Technologies Used

- **LangGraph + LangChain**: State orchestration
- **FastAPI**: Backend APIs
- **Angular (standalone)**: Frontend interface
- **Ollama**: LLM-powered classification
- **API Ninja**: Geodata & demographics
- **PostgreSQL**: Persistent storage
- **Selenium**: Form automation

---

## 📸 Screenshots
![Screenshot (474)](https://github.com/user-attachments/assets/166df13a-2f5e-47e3-8742-cf3592f08173)
![Screenshot (473)](https://github.com/user-attachments/assets/270d4085-e64f-4e28-80d7-27e519e2ea98)
![Screenshot (472)](https://github.com/user-attachments/assets/0315661f-8ae6-4e01-a872-82893716f529)



---

## 🙌 Acknowledgements

This wasn’t thrown together. Every piece — from the API integration to the form logic — was built with focus and determination.

Thanks for reading this far. It means a lot.

If you're a recruiter, engineer, or mentor: I’m open to opportunities where I can keep doing this kind of work, but better, with a team.

Sincerely,  
**Harianth Kalavala**
