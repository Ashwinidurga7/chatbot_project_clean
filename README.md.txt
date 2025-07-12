# Chatbot Project with Message Deletion Feature

This is a simple web-based chatbot project built using **Flask**, **HTML/CSS/JavaScript**, and **Google Gemini API**. The chatbot supports:

* Conversational interface using the Gemini API
* Chat history display
* Ability to delete messages
* Display of deleted messages separately

---

## 📁 Project Structure

```
chatbot_project_clean/
├── app.py                # Flask backend logic
├── templates/
│   └── index.html        # Chatbot UI (HTML + CSS + JS)
├── chat_history.json     # Chat history (auto-saved)
├── deleted_messages.json # Deleted messages (auto-saved)
├── .env                  # Stores API key
├── requirements.txt      # Python dependencies
```

---

## 🚀 How to Run This Project

### 1. Clone or Download the Project

```bash
cd Downloads
cd chatbot_project_clean
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Create a `.env` file in the root folder and paste:

```
GEMINI_API_KEY=your_key_here
```

Replace `your_key_here` with your actual Gemini API key.

### 5. Start the Flask Server

```bash
python app.py
```

Go to [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧠 Features

* Gemini-powered bot responses
* Clean UI with CSS styling
* User and bot messages
* Delete any message with a button
* See all deleted messages in a separate section

---

## 📦 Dependencies (requirements.txt)

```txt
flask
python-dotenv
google-generativeai
```

Generate it using:

```bash
pip freeze > requirements.txt
```

---

## 📝 Notes

* This project is meant for **learning/demo purposes**.
* Gemini API usage may require quota limits.

---

## 💡 Credits

Developed as a chatbot project using Gemini API and Flask.

