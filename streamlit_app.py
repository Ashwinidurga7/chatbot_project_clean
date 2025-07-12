import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Set up Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found. Please set it in Streamlit Cloud secrets or your local .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []
if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel("gemini-pro").start_chat()

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("💬 Gemini Chatbot")
st.caption("Powered by Google's Gemini API")

# Display chat history
for item in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(item["user"])
    with st.chat_message("assistant"):
        st.markdown(item["bot"])

# User input
prompt = st.chat_input("Type your message...")
if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to Gemini and get response
    try:
        response = st.session_state.chat.send_message(prompt)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"

    # Show bot reply
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save to history
    st.session_state.history.append({"user": prompt, "bot": bot_reply})

# Trigger rebuild - Gemini setup confirmed







