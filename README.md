# 🧠 Reddit Persona Builder

This project analyzes a Reddit user’s public activity to generate a detailed user persona using a local LLM (like `llama3` via [Ollama](https://ollama.com)).



## 🚀 Features

- Scrapes posts & comments from a Reddit user
- Generates a user persona (profession, hobbies, personality)
- Cites post/comment numbers as evidence
- Uses local LLM (Ollama)
- Outputs persona to a `.txt` file



## 🧑‍💻 Setup

### 1. Clone & Create Virtual Environment

```bash
git clone https://github.com/yourusername/reddit-persona
cd reddit-persona
python -m venv reddit_env
.\reddit_env\Scripts\activate       # Windows
# or source reddit_env/bin/activate  # Mac/Linux


### 2. Install Dependencies

```bash
pip install -r requirements.txt


### 3. Set Reddit API Credentials

Create a `.env` file with:


REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=persona_bot/0.1 by your_reddit_username
```

> Get these from [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)


## 🧠 Using Ollama (LLM)

Install and run [Ollama](https://ollama.com) locally:

```bash
ollama pull llama3

## ▶️ Run the Project

```bash
python main.py


Enter a Reddit user profile like:


https://www.reddit.com/user/kojied/

## 📄 Output

The result is saved as:


persona_kojied.txt


Includes personality, hobbies, and citations like "Post #2".



## 📁 Project Structure

├── main.py
├── reddit_client.py
├── local_llm.py
├── .env
├── requirements.txt
└── persona_*.txt


## ⚠️ Note

* Only works with **user profiles**, not subreddits.
* Requires meaningful public activity to generate useful output.

