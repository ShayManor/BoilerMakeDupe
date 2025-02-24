import datetime
from config import db

def store_agent(name, description, model, repo_url, icon_url, frn):
    """Stores an AI agent in MongoDB with a GitHub link, an icon URL, and an FRN (IP address)."""
    agent_data = {
        "name": name,
        "description": description,
        "model": model,
        "repo_url": repo_url,
        "icon_url": icon_url,  # New field for storing the icon url
        "FRN": frn,  # New field for storing the agent's IP address
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }

    db.agents.insert_one(agent_data)
    print(f"✅ Stored agent '{name}' with GitHub link: {repo_url}, icon: {icon_url}, and FRN: {frn}")

def get_agent(name):
    """Fetches an AI agent from MongoDB."""
    agent = db.agents.find_one({"name": name}, {"_id": 0})

    if agent:
        print(f"✅ Agent found: {agent}")
        return agent
    else:
        print(f"❌ No agent named '{name}' found.")
        return None

def update_agent(name, new_description=None, new_repo_url=None, new_icon_url=None, new_frn=None):
    """Updates an AI agent’s details in MongoDB."""
    update_fields = {"updated_at": datetime.datetime.utcnow()}

    if new_description:
        update_fields["description"] = new_description
    if new_repo_url:
        update_fields["repo_url"] = new_repo_url
    if new_icon_url:
        update_fields["icon_url"] = new_icon_url  # Allow updating the icon URL
    if new_frn:
        update_fields["FRN"] = new_frn  # Allow updating the agent's IP address (FRN)

    result = db.agents.update_one({"name": name}, {"$set": update_fields})

    if result.matched_count:
        print(f"✅ Updated agent '{name}'.")
    else:
        print(f"❌ No agent named '{name}' found.")

def delete_agent(name):
    """Deletes an AI agent from MongoDB."""
    result = db.agents.delete_one({"name": name})

    if result.deleted_count:
        print(f"🗑️ Deleted agent '{name}'.")
    else:
        print(f"❌ No agent named '{name}' found.")
