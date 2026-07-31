import os
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

# ----------------------------------------
# Load API Key
# ----------------------------------------
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------------------------------
# Read PDF
# ----------------------------------------
try:
    reader = PdfReader("sample.pdf")
except FileNotFoundError:
    print("❌ sample.pdf not found!")
    exit()

text = ""

# Read ONLY the first 2 pages
for i, page in enumerate(reader.pages):
    if i >= 2:
        break

    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

print("✅ PDF loaded successfully!")
print(f"📄 Total Pages in PDF: {len(reader.pages)}")
print("📖 Sending only the first 2 pages to Gemini...\n")

# ----------------------------------------
# Ask Gemini
# ----------------------------------------
try:
    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=f"""
You are an AI assistant.

Read the following PDF content and provide:

1. A short summary
2. Main topics
3. Important points in bullet form

PDF Content:

{text}
"""
    )

    print("=" * 60)
    print("📚 AI SUMMARY")
    print("=" * 60)
    print(response.text)

except Exception as e:
    print("\n❌ Gemini API Error")
    print("=" * 60)
    print(e)
    print("=" * 60)