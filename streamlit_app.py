import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY not found. Please set it in Streamlit secrets or .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit App UI
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")
st.caption("Powered by Google's Gemini Pro")

# Show history
for item in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(item["user"])
    with st.chat_message("assistant"):
        st.markdown(item["bot"])

# Input
prompt = st.chat_input("Ask me anything...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = st.session_state.chat.send_message(prompt)
        reply = response.text
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save conversation
    st.session_state.history.append({"user": prompt, "bot": reply})
