# 🚀 WhatsApp Scam Detection System

An AI-powered WhatsApp bot that detects scam, phishing, and fraudulent messages in real-time using a hybrid detection engine (rule-based + AI logic).

---

## 🔍 Overview

This project is designed to identify potentially harmful WhatsApp messages such as:

* Gold investment scams
* Bank/KYC fraud messages
* Phishing links and malicious URLs
* APK / fake app download traps
* Fake offers, lottery, and prize scams

The system analyzes incoming messages via webhook, assigns a risk score, and responds with **bilingual alerts (English + Telugu)** to improve user awareness and safety.

---

## ✨ Key Features

* ⚡ Real-time WhatsApp message processing
* 🧠 Hybrid scam detection (rule-based + AI-ready architecture)
* 📊 Risk scoring system (Low / Medium / High)
* 🌐 Bilingual alerts (English + Telugu)
* 🔗 Detection of phishing links & suspicious keywords
* 📦 Modular backend architecture (production-ready structure)
* 🗄️ MongoDB integration for message storage & analytics

---

## 🏗️ System Architecture

User (WhatsApp)
⬇
Twilio Webhook
⬇
FastAPI Backend
⬇
Message Processor
⬇
AI Analyzer + Risk Engine
⬇
Response Generator (Bilingual Warning)

---

## 🛠️ Tech Stack

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| FastAPI               | Backend API & webhook handling |
| Python                | Core logic & processing        |
| MongoDB               | Data storage                   |
| Twilio API            | WhatsApp integration           |
| OpenAI API (optional) | Advanced AI analysis           |
| Uvicorn               | ASGI server                    |

---

## 📂 Project Structure

```
whatsapp-fake-detector/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── db/
│   ├── config/
│   └── requirements.txt
│
├── screenshots/
├── README.md
└── .gitignore
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/whatsapp-fake-detector.git
cd whatsapp-fake-detector
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r backend/requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside `backend/`:

```
OPENAI_API_KEY=your_openai_key
MONGO_URI=your_mongodb_uri
```

### 5. Run the server

```
python -m uvicorn backend.main:app --reload
```

---

## 📸 Demo Screenshots
![image alt](https://github.com/parnapallimunicharitha-crypto/whatsapp-fake-detector/blob/main/backend/Screenshot%202026-04-30%20211905.png?raw=true
)
![image alt]("https://github.com/parnapallimunicharitha-crypto/whatsapp-fake-detector/blob/main/backend/Screenshot%202026-04-30%20210844.png?raw=true)
![image alt](https://github.com/parnapallimunicharitha-crypto/whatsapp-fake-detector/blob/main/backend/Screenshot%202026-04-30%20210111.png?raw=true)
![image alt](https://github.com/parnapallimunicharitha-crypto/whatsapp-fake-detector/blob/main/backend/Screenshot%202026-04-30%20210140.png?raw=true)

---

## 🚀 How It Works

1. User sends a message on WhatsApp
2. Twilio forwards it to FastAPI webhook
3. Message is analyzed using detection engine
4. Risk score is calculated
5. User receives a warning message instantly

---

## 📈 Future Enhancements

* 🔗 Real-time URL reputation checking
* 📊 Admin dashboard for analytics
* 🤖 ML model for advanced fraud detection
* 📱 Mobile app integration
* 🌍 Multi-language support

---

## 💼 Resume Highlights

* Built a real-time WhatsApp Scam Detection System using FastAPI and Twilio API
* Implemented hybrid fraud detection (rule-based + AI-ready system)
* Designed bilingual alert system for improved user awareness
* Integrated MongoDB for scalable data storage and analytics
* Developed modular and production-ready backend architecture

---

## 👤 Author

**Parnapalli Muni Charitha**
B.Tech Student | Aspiring Software Developer

---

## ⭐ If you found this useful

Give this repo a ⭐ and share it!
