# Rude AI Chatbot (Groq + FastAPI + Render + Python GUI)

A chaotic, sarcastic AI chatbot powered by Groq’s LLaMA‑3.3‑70B model, served through a FastAPI backend on Render, and accessed via either a Python CLI or a Tkinter GUI.

---

## 🧠 Overview

This project contains:

- A FastAPI backend deployed on Render
- A Groq-powered AI personality (“rude gremlin roommate”)
- A Python CLI client
- A Tkinter GUI client
- A simple /chat endpoint that accepts user messages and returns AI replies

---

## 🏗️ Project Structure

    root/
    │
    ├── chat.py              # CLI client
    ├── chat_gui.py          # Tkinter GUI client
    ├── server.py            # FastAPI backend using Groq API
    ├── render.yaml          # Render deployment config
    ├── requirements.txt     # Python dependencies
    └── README.md

---

## ⚙️ Tech Stack

- FastAPI
- Groq Python SDK
- Render (backend hosting)
- Python Requests
- Tkinter GUI
- Uvicorn ASGI server

---

## 🔐 Environment Variables

Your backend requires:

    GROQ_API_KEY=your_groq_api_key_here

This must be set in Render, not committed to GitHub.

---

## 🚀 Backend (FastAPI on Render)

### Endpoint

    POST /chat

### Request Body

    {
      "message": "your text here"
    }

### Response

    {
      "reply": "AI response text"
    }

### Backend Logic Summary

- Loads GROQ_API_KEY from environment variables
- Creates a Groq client
- Defines /chat endpoint
- Sends system + user messages to Groq
- Returns the AI’s reply

---

## 🌐 Render Deployment

### render.yaml

    services:
    - type: web
      name: rude-backend
      env: python
      buildCommand: pip install -r requirements.txt
      startCommand: uvicorn server:app --host 0.0.0.0 --port 10000


## 💬 Python CLI Client

Run:

    python chat.py

Example:

    You: hello
    AI: oh wow, THAT’S what you decided to open with?

---

## 🖥️ Tkinter GUI Client

Run:

    python chat_gui.py

Features:

- Cyan = user
- Magenta = AI
- Press Enter or click Send

---

## 🛠️ Local Development

Start backend locally:

    uvicorn server:app --reload

Run CLI:

    python chat.py

Run GUI:

    python chat_gui.py

---

## 🧪 Testing the API

    curl -X POST https://rude-backend.onrender.com/chat \
         -H "Content-Type: application/json" \
         -d '{"message":"hello"}'

---

## 📝 Notes

- Groq API key must never be committed
- Render handles HTTPS automatically
- Backend is stateless — no database needed
- AI personality is controlled entirely by the system prompt
