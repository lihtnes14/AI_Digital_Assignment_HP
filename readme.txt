# 💬 Lendora LangGraph Chatbot

A blazing-fast **Streamlit web app** that lets you **chat seamlessly with an AI assistant** powered by **LangGraph** and **Groq’s LLM** (`gemma2-9b-it`). Designed for responsiveness, clarity, and streaming conversations in real time.

## ✨ Features

- ⚡ **Ultra-fast responses**: Powered by Groq’s `gemma2-9b-it` model for near-instantaneous replies.
- 🧠 **LangGraph-powered state logic**: Structured node-based graph for handling conversations.
- 🔁 **Streaming responses**: Smooth message streaming with real-time updates.
- 💬 **Conversation memory**: Retains chat history with Streamlit's `session_state`.
- 🎨 **Minimal, centered UI**: Clean and focused chat interface built with Streamlit.

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **LLM:** Groq `gemma2-9b-it`
- **State Management:** LangGraph (`StateGraph`, `TypedDict`)
- **Streaming & Display:** Streamlit’s `chat_message` API
- **Secrets Management:** Python-dotenv (`.env` file)

---

## 🚀 Getting Started

Follow these steps to set up and run the app locally:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/lendora-langgraph-chatbot.git
cd lendora-langgraph-chatbot
