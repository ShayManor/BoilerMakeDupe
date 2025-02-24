from flask import Flask, request, jsonify
from agent_crud import store_agent, get_agent, update_agent, delete_agent

app = Flask(__name__)


@app.route("/agents", methods=["POST"])
def create_agent():
    """API endpoint to create an agent."""
    data = request.json

    # Validate required fields
    required_fields = ["name", "description", "model", "repo_url", "icon_url", "frn"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    store_agent(
        data["name"],
        data["description"],
        data["model"],
        data["repo_url"],
        data["icon_url"],
        data["frn"]
    )
    return jsonify({"message": "✅ Agent created successfully"}), 201


@app.route("/agents/<name>", methods=["GET"])
def get_agent_api(name):
    """API endpoint to retrieve an agent."""
    agent = get_agent(name)
    if agent:
        return jsonify(agent)
    return jsonify({"error": "❌ Agent not found"}), 404


@app.route("/agents/<name>", methods=["PUT"])
def update_agent_api(name):
    """API endpoint to update an agent."""
    data = request.json

    update_agent(
        name,
        new_description=data.get("description"),
        new_repo_url=data.get("repo_url"),
        new_icon_url=data.get("icon_url"),  # Fix: Allow updating icon
        new_frn=data.get("frn")  # Fix: Allow updating FRN (IP address)
    )

    return jsonify({"message": f"✅ Agent '{name}' updated."})


@app.route("/agents/<name>", methods=["DELETE"])
def delete_agent_api(name):
    """API endpoint to delete an agent."""
    delete_agent(name)
    return jsonify({"message": f"🗑️ Agent '{name}' deleted."})


if __name__ == "__main__":
    app.run(debug=True)
