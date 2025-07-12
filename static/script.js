<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>💬 Gemini Chatbot</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/static/style.css" />
  <style>
    body {
      margin: 0;
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(to right, #f2f2f2, #e6ecf0);
      display: flex;
      justify-content: center;
      padding: 30px 15px;
    }

    .chat-container {
      background: #ffffff;
      width: 100%;
      max-width: 700px;
      padding: 20px;
      border-radius: 16px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    #chat-box {
      height: 450px;
      overflow-y: auto;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 10px;
      background-color: #fefefe;
      margin-bottom: 15px;
    }

    .message {
      margin: 10px 0;
      padding: 10px 14px;
      border-radius: 12px;
      position: relative;
      max-width: 80%;
      line-height: 1.5;
    }

    .user {
      background-color: #dcf8c6;
      align-self: flex-end;
      margin-left: auto;
    }

    .bot {
      background-color: #f1f0f0;
      align-self: flex-start;
      margin-right: auto;
    }

    .message strong {
      display: block;
      font-size: 13px;
      margin-bottom: 4px;
      color: #555;
    }

    .input-area {
      display: flex;
      gap: 10px;
      margin-top: 10px;
    }

    #user-input {
      flex: 1;
      padding: 12px;
      border-radius: 10px;
      border: 1px solid #ccc;
      font-size: 16px;
    }

    button {
      padding: 12px 20px;
      border: none;
      border-radius: 10px;
      background-color: #007bff;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    .delete-btn {
      position: absolute;
      right: 10px;
      bottom: 8px;
      background-color: transparent;
      border: none;
      color: red;
      font-size: 12px;
      cursor: pointer;
    }

    .deleted-section {
      margin-top: 30px;
      background: #fff4f4;
      border: 1px solid #f8d7da;
      padding: 12px;
      border-radius: 10px;
    }

    .deleted-section h4 {
      margin-top: 0;
      margin-bottom: 10px;
      color: #a94442;
    }

    #deleted-messages li {
      font-size: 14px;
      margin-bottom: 6px;
      color: #a94442;
    }
  </style>
</head>
<body>
  <div class="chat-container">
    <h2>💬 Gemini Chatbot</h2>
    <div id="chat-box"></div>
    <div class="input-area">
      <input type="text" id="user-input" placeholder="Type a message..." />
      <button onclick="sendMessage()">Send</button>
    </div>
    <div class="deleted-section">
      <h4>📂 Deleted Messages</h4>
      <ul id="deleted-messages"></ul>
    </div>
  </div>

  <script>
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const deletedMessages = document.getElementById("deleted-messages");

    function appendMessage(sender, text) {
      const div = document.createElement("div");
      div.className = `message ${sender}`;

      const label = document.createElement("strong");
      label.textContent = sender === "user" ? "👨 You" : "🤖 Bot";

      const span = document.createElement("span");
      span.textContent = text;

      const deleteBtn = document.createElement("button");
      deleteBtn.className = "delete-btn";
      deleteBtn.textContent = "🗑";
      deleteBtn.onclick = () => deleteMessage(div, sender, text);

      div.appendChild(label);
      div.appendChild(span);
      div.appendChild(deleteBtn);

      chatBox.appendChild(div);
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    function deleteMessage(element, sender, text) {
      const li = document.createElement("li");
      li.textContent = `${sender === "user" ? "👨 You" : "🤖 Bot"}: ${text}`;
      deletedMessages.appendChild(li);
      element.remove();

      fetch("/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sender, text })
      });
    }

    async function sendMessage() {
      const message = userInput.value.trim();
      if (!message) return;

      appendMessage("user", message);
      userInput.value = "";

      try {
        const res = await fetch("/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message })
        });

        const data = await res.json();
        appendMessage("bot", data.response || "⚠️ No response.");
      } catch (e) {
        appendMessage("bot", "⚠️ Error reaching server.");
      }
    }

    userInput.addEventListener("keypress", e => {
      if (e.key === "Enter") sendMessage();
    });
  </script>
</body>
</html>











