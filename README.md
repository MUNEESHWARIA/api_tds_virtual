# TDS Virtual TA

This project is built as part of the Tools in Data Science course at IITM Online BS Program.

## Features
- REST API endpoint `/api/` for answering student questions.
- Returns dummy data with an answer and helpful links.
- Deployed using Railway (or Vercel/Render/Heroku).

## Usage
Send a POST request with a question in JSON:
```bash
curl -X POST https://your-app.up.railway.app/api/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the deadline for the GA5 assignment?"}'
