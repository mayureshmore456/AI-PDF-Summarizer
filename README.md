# AI PDF Summarizer

An AI-powered PDF summarizer built using Python and Google's Gemini API.

## Features

- Read PDF files
- Extract text using PyPDF
- Summarize PDF content with Gemini AI
- Error handling for API failures

## Technologies Used

- Python
- Google Gemini API
- PyPDF
- python-dotenv

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```

Place your PDF in the project folder and name it:

```
sample.pdf
```

Run:

```bash
python3 app.py
```

## Future Improvements

- Chat with PDFs (RAG)
- Semantic Search
- Vector Database
- Multi-document support