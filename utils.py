import os

def extract_username(url: str) -> str:
    return url.rstrip("/").split("/")[-1]

def save_to_file(username: str, persona_text: str):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)
