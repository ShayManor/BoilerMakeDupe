import os
import time

from openai import OpenAI

from .enums import *
from .create_ask_ai import create_ask_ai
from .create_requirements import create_requirements
from .create_app import create_app
from .create_run import create_run
from .create_index import create_index
from .upload_github import upload_to_github


def main(agent: AGENT):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    agent_abs_path = os.path.abspath(os.path.join(base_dir, agent.path))

    if not os.path.exists(agent_abs_path):
        os.makedirs(agent_abs_path)

    os.chdir(agent_abs_path)

    agent_folder = os.path.join(agent_abs_path, agent.name)
    os.makedirs(os.path.join(agent_folder, "templates"), exist_ok=True)
    os.chdir(base_dir)

    ask_ai = create_ask_ai(agent.model)
    with open(os.path.join(agent_folder, "ask_ai.py"), "w") as file:
        file.write(ask_ai)
    app = create_app(agent.description).replace('```python', '').replace('```', '')
    with open(os.path.join(agent_folder, "application.py"), "w") as file:
        file.write(app)

    run = create_run(app).replace('```bash', '').replace('```', '')
    with open(os.path.join(agent_folder, "run.sh"), "w") as file:
        file.write(run)
    index = create_index(app, agent.description).replace('```html', '').replace('```', '')
    with open(os.path.join(agent_folder, "templates/index.html"), "w") as file:
        file.write(index)

    create_requirements(agent.path, agent.name)
    git_link = upload_to_github(agent_abs_path)
    return agent.model

# t = time.time()
# a = AGENT()
# a.name = "bread-seller-predictor"
# a.description = "You are a essay writing helper who will give good feedback to improve and contain a text editor to get quick live changes. There should be a screen that I can put in an essay (as well as an example to test) and I should get help on it to improve."
# a.path = "../../Agents"
# main(a)
# print(f"Time taken: {time.time() - t}")

# You are a math teacher who will test students with good questions and tell them why they got it wrong if they do. Make easy, medium, and hard and go from 4th grade to college level math. Make sure these are good questions and it is easy for the user to use.
