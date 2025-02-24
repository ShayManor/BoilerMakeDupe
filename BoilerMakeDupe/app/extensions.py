import os
from openai import OpenAI
from pymongo import MongoClient

# Environment variables and configuration
MONGO_URI = os.environ.get(
    'MONGO_URI',
    'mongodb+srv://trueflash42:dOKpvn6cqAyK7RHb@agent.ctwv3.mongodb.net/boilermake25?retryWrites=true&w=majority&appName=Agent'
)
QUESTION_ASKER_ID = "asst_TlqR8FmQyvlUwkosUpu9Alk5"
conversation_data = {}

def gpt(prompt: str, assistant_id):
    client = OpenAI()
    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
    thread = client.beta.threads.create(
        messages=[{"role": "user", "content": prompt}]
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        ai_response = messages.data[0].content[0].text.value
        return ai_response
    return ""

# Initialize MongoDB connection
try:
    client = MongoClient(MONGO_URI)
    db = client['boilermake25']
    agents_collection = db['agents']
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("Error connecting to MongoDB:", e)
    agents_collection = None
