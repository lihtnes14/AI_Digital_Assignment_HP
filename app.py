import streamlit as st
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv()

# Set API keys in the environment (or manually input if using secrets)


# Initialize LLM
llm = ChatGroq(
    api_key="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",
    model_name="gemma2-9b-it"
)

# Define State for LangGraph
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# Node logic
def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

# Streamlit UI
st.set_page_config(page_title="LangGraph Chatbot", layout="centered")
st.title("💬 Lendora Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Say something...")

# Show history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Process input
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream LangGraph response
    full_response = ""
    with st.chat_message("assistant"):
        response_box = st.empty()
        for event in graph.stream({"messages": ("user", user_input)}):
            for value in event.values():
                if "messages" in value:
                    msg = value["messages"]
                    full_response = msg.content
                    response_box.markdown(full_response)

    st.session_state.chat_history.append(("assistant", full_response))
