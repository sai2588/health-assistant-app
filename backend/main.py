
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, ChatLog

Base.metadata.create_all(bind=engine)

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


class QueryRequest(BaseModel):
    prompt: str


async def fetch_from_openrouter(prompt: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://your-app-url.com",
        "X-Title": "Health Assistant App"
    }

    payload = {
        "model": "openai/gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to contact OpenRouter")

    return response.json()


@app.post("/generate")
async def generate_text(request: QueryRequest):
    response_data = await fetch_from_openrouter(request.prompt)
    response_text = response_data['choices'][0]['message']['content']

    db = SessionLocal()
    chat_log = ChatLog(prompt=request.prompt, response=response_text)
    db.add(chat_log)
    db.commit()

    return {"response": response_text}
            