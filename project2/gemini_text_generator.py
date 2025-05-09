import requests
import gradio as gr

API_KEY = "your_api_key_here"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_text(prompt, word_limit=100):
    full_prompt = f"Generate a text with a word limit of {word_limit} words:\n\n{prompt}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": full_prompt}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Response received, but the format is not as expected."
    else:
        return f"Erreur {response.status_code} : {response.text}"

# Interface Gradio
interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=3, placeholder="Enter your prompt here", label="Input Prompt"),
        gr.Slider(50, 500, step=50, label="Word Limit")
    ],
    outputs=gr.Textbox(label="Generated Text"),
    title="Text Generator (Gemini API)",
    description="Uses Gemini 2.0 Flash to generate text with a word limit."
)

if __name__ == "__main__":
    interface.launch(share=True)
