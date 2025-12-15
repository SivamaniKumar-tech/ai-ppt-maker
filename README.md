\# AI Presentation Maker 🎯



An AI-powered academic presentation generator that creates professional PowerPoint decks using a reusable template engine.



\## 🚀 Features

\- Topic → AI-generated structured outline (OpenAI)

\- Template-driven PPT generation (python-pptx)

\- Consistent academic design

\- Flask API with download endpoint

\- Secure API key handling via `.env`



\## 🧠 Tech Stack

\- Python, Flask

\- OpenAI API

\- python-pptx

\- PowerShell (Windows)

\- Git \& GitHub



\## 📦 How it works

1\. User sends a topic

2\. AI generates a structured JSON outline

3\. Template engine injects content into PPT

4\. PPT is generated and downloadable



\## ▶️ Run locally

```bash

python -m venv .venv

.\\.venv\\Scripts\\activate

pip install -r requirements.txt

python app.py







📌 Example API call



POST /generate

{

&nbsp; "topic": "Zero Trust Security"

}



