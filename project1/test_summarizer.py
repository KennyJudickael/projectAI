import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error: {response.status_code} - {response.text}"
