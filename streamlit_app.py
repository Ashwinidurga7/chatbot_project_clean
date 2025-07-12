# streamlit_app.py

import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not set. Please add in Settings → Secrets")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Gemini Chatbot")
st.title("🤖 Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        reply = response.text
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})






