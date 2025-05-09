import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"  # Example API URL for OLLAMA

def generate_text(prompt, world_limit=100):

    full_prompt = f"Generate a text with a word limit of {world_limit} words:\n\n{prompt}"

    payload = {
        "model": "deepseek-r1",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error: {response.status_code} - {response.text}"



# if __name__ == "__main__":

#     prompt = "Write a short story about a dragon and a knight."
#     print("Generated text:")
#     print(generate_text(prompt))

# Gradio Interface
# Create a Gradio interface for the text generation function
interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=3, placeholder="Enter your prompt here", label="Input Prompt"),
        gr.Slider(50, 500,step=50, label="Word Limit")
    ],
    outputs=gr.Textbox(label="Generated Text"),
    title="Text Generator",
    description="Enter a prompt to generate text with a specified word limit using the DeepSeek model."
    )
if __name__ == "__main__":
    # Launch the Gradio app
    interface.launch(share=True)  # Set share=True to get a public link for the app
