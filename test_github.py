from github import Github, Auth
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

# -------------------------
# Test GitHub
# -------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

# Get authenticated user
user = g.get_user()
print(f"👤 GitHub Authenticated as: {user.login}")

if user.login != USERNAME:
    print(f"⚠️ Warning: .env username ({USERNAME}) doesn't match actual login ({user.login})")

print("\n📂 Your first 5 GitHub repos:")
for repo in user.get_repos()[:5]:
    print("-", repo.name)

# -------------------------
# Test OpenAI
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIxZjEwMDEzMTdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.6o32UKZgcB6Azjq7gSVEwHOp-1f5EAoxqD02tLrfq94"
client = OpenAI(api_key=OPENAI_API_KEY)

try:
    response = client.models.list()
    print("\n✅ OpenAI Authenticated. Available models:")
    for m in response.data[:5]:
        print("-", m.id)
except Exception as e:
    print("\n❌ OpenAI API failed:", e)
