import requests

def ask_ai(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "dinesh",  # Replace with your model like "mistral", "llama2", etc.
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error connecting to local Ollama: {e}"
