from reddit_client import scrape_user_data
from local_llm import build_prompt, run_ollama
from utils import extract_username, save_to_file

def generate_persona(url):
    username = extract_username(url)
    print(f"[+] Fetching data for u/{username}...")
    posts, comments = scrape_user_data(username)
    
    if not posts and not comments:
        print("[-] No data found.")
        return

    print("[+] Building prompt...")
    prompt = build_prompt(posts, comments)

    print("[+] Running local LLM (Ollama)...")
    persona = run_ollama(prompt)

    print("[+] Saving persona...")
    save_to_file(username, persona)
    print(f"[✓] Done: output/{username}_persona.txt")

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ").strip()
    generate_persona(url)
