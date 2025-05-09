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


if __name__ == "__main__":

    sample_text = """
        Genshin Impact is an open-world action role-playing game developed and published by miHoYo. It was released for Microsoft Windows, PlayStation 4, Nintendo Switch, iOS, and Android. The game features a fantasy world called Teyvat, which is home to seven distinct nations, each of which is based on a different culture and element. Players take on the role of the Traveler, who is searching for their lost sibling and unraveling the mysteries of Teyvat.
     """
    print("Summerize text:")
    print(summarize_text(sample_text))
