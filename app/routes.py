from flask import Blueprint, render_template, request, jsonify
import uuid
from app.extensions import agents_collection, conversation_data, gpt, QUESTION_ASKER_ID
from Helpers.Creator.create_files import main
from Helpers.Creator.enums import AGENT

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create')
def create_page():
    return render_template('create.html')

# Commented out unless needed
# @bp.route('/about')
# def about():
#     return render_template('about.html')

@bp.route('/create_agent', methods=['POST'])
def create_agent():
    try:
        data = request.get_json()
        agent_name = data.get('agentName')
        description = data.get('description')

        if not agent_name or not description:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if the agent already exists.
        existing_agent = agents_collection.find_one({'agentName': agent_name})
        if existing_agent:
            message = f"Agent '{agent_name}' already exists."
            status = "exists"
            return jsonify({"status": status, "message": message})

        # Generate a new conversation ID.
        conversation_id = str(uuid.uuid4())
        conversation_data[conversation_id] = {
            "agentName": agent_name,
            "description": description
        }

        initial_prompt = f"Agent Name: {agent_name}\nDescription: {description}\nPlease ask a question to refine the assistant."
        initial_question = gpt(initial_prompt, QUESTION_ASKER_ID)

        return jsonify({"conversationId": conversation_id, "question": initial_question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/create_agent/continue', methods=['POST'])
def continue_conversation():
    try:
        data = request.get_json()
        conversation_id = data.get('conversationId')
        chat_log = data.get('chatLog')  # The entire conversation log as a single string.
        if not conversation_id or not chat_log:
            return jsonify({"error": "Missing conversationId or chatLog"}), 400

        # Pass the entire chat log to GPT.
        ai_response = gpt(chat_log, QUESTION_ASKER_ID)
        if not ai_response or ai_response.strip() == "" or ai_response.strip().lower() == "none":
            ai_response = "Creating your agent, please wait..."

        if ai_response.strip().upper() == "DONE":
            # Retrieve the initial agent info.
            agent_info = conversation_data.get(conversation_id)
            if not agent_info:
                return jsonify({"error": "Conversation data not found"}), 400

            # Create the agent (simulate creation by calling main).
            agent = AGENT()
            agent.name = agent_info["agentName"]
            agent.description = agent_info["description"]
            agent.avatarUrl = "avatarUrl"
            agent.FRN = "frn"
            agent.modelType = agent_info["modelType"]
            main(agent)

            # Insert the new agent into MongoDB.
            new_agent = {
                "agentName": agent.name,
                "description": agent.description,
                "modelType": agent.modelType,
                "avatarUrl": agent.avatarUrl,
                "FRN": agent.FRN,
                "flag": "default"
            }
            agents_collection.insert_one(new_agent)

            # Remove conversation data.
            del conversation_data[conversation_id]

            return jsonify({"message": "Agent creation complete.", "finished": True})
        else:
            return jsonify({"message": ai_response, "finished": False})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/agent/<agent_name>', methods=['GET'])
def get_agent(agent_name):
    try:
        agent = agents_collection.find_one({'agentName': agent_name})
        if agent:
            agent['_id'] = str(agent['_id'])
            return jsonify(agent)
        else:
            return jsonify({"error": "Agent not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/api/agents', methods=['GET'])
def get_all_agents():
    try:
        agents = list(agents_collection.find())
        for agent in agents:
            agent['_id'] = str(agent['_id'])
        return jsonify({"agents": agents})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/agents', methods=['GET'])
def agents_page():
    return render_template('agents.html')
