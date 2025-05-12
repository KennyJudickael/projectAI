from fastapi import FastAPI
import requests
import re

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"  # Example API URL for OLLAMA

@app.post("/generate/")
def generate_text(prompt: str, world_limit: int = 100):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Generate a text with a word limit of {world_limit} words:\n\n{prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    text = response.json().get("response", "No response found")

    # Enlever tout ce qui est entre <think>...</think>
    cleaned_text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL)

    return {cleaned_text.strip()}

#run with: python -m uvicorn app:app --reload
