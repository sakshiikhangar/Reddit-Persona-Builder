import subprocess

def build_prompt(posts, comments):
    combined = "\n\n".join(
        [f"Post {i+1}: {p}" for i, p in enumerate(posts)] +
        [f"Comment {i+1}: {c}" for i, c in enumerate(comments)]
    )
    prompt = f"""Analyze the Reddit user's posts and comments below to build a detailed user persona. 
List traits like profession, hobbies, values, personality traits, etc., and cite Post # or Comment # where possible.

{combined}
"""
    return prompt

def run_ollama(prompt, model="llama3"):
    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Encode prompt to UTF-8 to avoid UnicodeEncodeError
    stdout, _ = process.communicate(input=prompt.encode("utf-8"))
    return stdout.decode("utf-8")
