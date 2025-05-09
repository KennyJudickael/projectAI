from fastapi import FastAPI
import requests

app = FastAPI()
Ollama_URL = "http://localhost:11434/api/generate"  # Example API URL for OLLAMA

@app.post("/summarize/")
def summarize_test(text: str):
    playload = {"model": "deepseek-r1", "prompt": f"Summarize the following text:\n\n{text}", "stream": False}
    response = requests.post(Ollama_URL, json=playload)
    return response.json().get("response", "No response found")

# run with: python -m uvicorn app:app --reload
