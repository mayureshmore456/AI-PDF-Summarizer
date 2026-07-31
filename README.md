# 📄 AI PDF Summarizer

An AI-powered PDF summarizer built using **Python**, **PyPDF**, and the **Google Gemini API**. The application extracts text from PDF documents and generates concise summaries using a Large Language Model (LLM).

---

## ✨ Features

- 📄 Read PDF documents
- 📝 Extract text using PyPDF
- 🤖 Generate AI-powered summaries with Gemini
- 🔐 Secure API key management using `.env`
- ⚠️ Basic API error handling
- 📚 Supports multi-page PDF documents

---

## 🛠️ Tech Stack

- Python 3
- Google Gemini API
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```
AI-PDF-Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── sample.pdf (user provides their own PDF)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mayureshmore456/AI-PDF-Summarizer.git
```

### 2. Move into the project

```bash
cd AI-PDF-Summarizer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 5. Add your PDF

Place your PDF inside the project folder and name it:

```
sample.pdf
```

### 6. Run the project

```bash
python3 app.py
```

---

## 🔄 Project Workflow

```
PDF File
     │
     ▼
Extract Text (PyPDF)
     │
     ▼
Prompt Creation
     │
     ▼
Gemini API
     │
     ▼
AI Generated Summary
```

---

## 📸 Example Output

```
✅ PDF loaded successfully!

📄 Total Pages: 2

============================
📚 AI SUMMARY
============================

• Main Topic 1
• Main Topic 2
• Important Concepts
• Key Takeaways
```

---

## 📚 What I Learned

While building this project I learned:

- Working with PDF files in Python
- Text extraction using PyPDF
- Sending long prompts to an LLM
- Prompt Engineering
- API integration
- Error handling
- Git & GitHub workflow

---

## 💡 Challenges Faced

One important challenge during development was that sending an entire PDF to the LLM exceeded request limits for larger documents.

This helped me understand why **Retrieval-Augmented Generation (RAG)** is used in modern AI applications. Instead of sending an entire document, RAG retrieves only the relevant sections before sending them to the LLM.

---

## 🚀 Future Improvements

- Chat with PDF documents
- Implement RAG
- Semantic Search
- Embeddings
- Vector Database Integration
- Multi-PDF support
- Streamlit Web Interface

---

## 👨‍💻 Author

**Mayuresh More**

Computer Engineering Student | Learning AI Engineering
