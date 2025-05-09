import requests

OLLAMA_URL = "http://localhost:11434/api/generate"  # Example API URL for OLLAMA

def query_ollama(prompt):
    playload ={
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=playload)
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error: {response.status_code} - {response.text}"

#testing the model
test_prompt = "What is genshin impact?"
print(query_ollama(test_prompt))
