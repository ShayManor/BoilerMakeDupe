import os
import subprocess
from config import db


def clone_agent(name, target_dir="/home/ubuntu/agents"):
    """Fetches the GitHub repo URL from MongoDB and clones it to the EC2 instance."""

    agent = db.agents.find_one({"name": name})
    if not agent:
        print(f"❌ No agent named '{name}' found in database.")
        return

    repo_url = agent["repo_url"]

    os.makedirs(target_dir, exist_ok=True)
    agent_dir = os.path.join(target_dir, name)

    if os.path.exists(agent_dir):
        print(f"⚠️ Agent '{name}' already exists. Pulling latest updates...")
        subprocess.run(["git", "-C", agent_dir, "pull"], check=True)
    else:
        print(f"🔄 Cloning agent '{name}' from {repo_url}...")
        subprocess.run(["git", "clone", repo_url, agent_dir], check=True)

    print(f"✅ Agent '{name}' is ready at {agent_dir}")