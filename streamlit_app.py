# streamlit_app.py

import streamlit as st
import google.generativeai as genai
import os

# Load Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY is not set. Please set it in Streamlit secrets.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title("💬 Gemini Chatbot")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini Response
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        reply = response.text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})




