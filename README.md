# 🛡️ Cybersecurity Expert Chatbot

A fully functional AI chatbot that simulates a highly experienced **Cybersecurity Expert**. This project leverages **Groq's LLM API** (`llama-3.3-70b-versatile`) on the backend (via Flask) and a modern, clean, and responsive HTML/CSS-based frontend. The assistant is designed to answer only cybersecurity-related queries and adheres to a strict domain persona.

---

## 📂 Project Structure

```
Cybersecurity-Expert-Chatbot/
├── chatbot_backend1.py     # Flask backend to handle Groq API communication
├── chatbot_frontend1.html  # Frontend chat interface
├── README.md               # Project documentation
```

---

## 🌐 Features

- 🔐 Responds only to cybersecurity-related questions
- 🧠 Persona-based system message for expert tone and context awareness
- 💬 Real-time message streaming from backend to frontend
- 🕵️‍♂️ Asks user's name before starting a conversation (context memory intro)
- 🧾 Local chat history saved in browser `localStorage`
- 🎨 Modern, clean UI with dark theme

---

## 🚀 Technologies Used

### Backend:
- **Python 3.11+**
- **Flask**
- **Groq SDK (`groq` Python library)**
- **LLM Model**: `llama-3.3-70b-versatile` (via Groq API)

### Frontend:
- HTML5, CSS3 
- JavaScript (for chat interaction and streaming)
- Responsive Design

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cybersecurity-chatbot.git
cd cybersecurity-chatbot
```

### 2. Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

pip install flask
pip install groq
```

### 3. Set Your Groq API Key

In `chatbot_backend1.py`, replace the placeholder with your actual API key:

```python
client = Groq(api_key="your_groq_api_key_here")
```

### 4. Run the Flask Server

```bash
python chatbot_backend1.py
```

The server will start at: `http://127.0.0.1:5002`

### 5. Open the Frontend

Open `chatbot_frontend1.html` in your web browser (preferably Chrome or Firefox).

---

## 🔁 Example Usage

1. User opens the page and is prompted for their name.
2. Types a question like:  
   ➤ *"What are the best practices for securing cloud infrastructure?"*
3. Chatbot responds in real-time using the Groq API.

---

## 🔐 Chatbot Persona Highlights

- ✅ Only answers cybersecurity questions
- 🚫 Refuses unrelated queries (e.g., history, movies, sports)
- 🧑‍💻 Expertise: Ethical hacking, cloud security, malware analysis, forensics
- 📌 CIA Triad principles strictly followed

---

## ✅ To-Do / Improvements

- [ ] Deploy backend on Render/Heroku
- [ ] Add file upload for cybersecurity reports/logs
- [ ] Use OpenAI/Groq streaming APIs more robustly with error handling
- [ ] Add support for multiple personas (e.g., Compliance Officer, Forensic Analyst)

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## ✍️ Author

Manish – AI/ML Enthusiast & Cybersecurity Bot Developer  
Connect with me on [LinkedIn](https://linkedin.com/in/manish-saini-9255aa28b) | GitHub: [Manish_Saini](https://github.com/Codergamer-2023)
