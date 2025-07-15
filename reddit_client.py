import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_user_data(username: str, limit=50):
    user = reddit.redditor(username)
    comments = [comment.body for comment in user.comments.new(limit=limit)]
    posts = [post.title + "\n" + post.selftext for post in user.submissions.new(limit=limit)]
    return posts, comments
