LENDORA CHATBOT
===============

Lendora Chatbot is a conversational AI assistant built using LangGraph, Streamlit, and Groq’s gemma2-9b-it model. It helps users interactively explore topics like deep learning (e.g., Convolutional Neural Networks) with intelligent prompts and personalized suggestions.

-------------------------
🔧 TECHNOLOGIES USED
-------------------------
- LangGraph (chat graph framework)
- LangChain-Groq (Groq API integration)
- Streamlit (UI framework)
- Python 3.11+
- dotenv (for managing environment variables)

-------------------------
🚀 SETUP INSTRUCTIONS
-------------------------

1. Clone the Repository
-----------------------
git clone <your-repo-url>
cd <your-repo-folder-name>

2. Create and Activate Virtual Environment
------------------------------------------
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate.bat    # Windows

3. Install Dependencies
------------------------
pip install -r requirements.txt

Create a `requirements.txt` file with the following:
----------------------------------------------------
streamlit
langchain
langgraph
langchain_groq
python-dotenv

4. Add Your API Key to a .env File
----------------------------------
Create a file named `.env` in the root directory and add:

GROQ_API_KEY=your_groq_api_key_here

5. Run the App
--------------
streamlit run app.py

Open the browser at: http://localhost:8501

-------------------------
💬 SAMPLE PROMPT
-------------------------
Hey, can you find me a course to master convolutional neural network?

-------------------------
📸 SCREENSHOT
-------------------------
Include this in the repo:
Screenshot 2025-04-21 at 17.48.50.png

-------------------------
✅ FEATURES
-------------------------
- Interactive conversational assistant
- Asks follow-up questions based on user's level
- Remembers multi-turn conversations
- Runs entirely on local machine

-------------------------
🧑‍💻 CREDITS
-------------------------
Built using LangGraph, Groq, and Streamlit.
