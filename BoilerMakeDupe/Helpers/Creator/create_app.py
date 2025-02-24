import os

from openai import OpenAI


def prompt_shell(desc, template):
    return f"You are a professional AI Agent developer who will take {desc} and create a new app. You will create the flask application.py file that is already partly filled in as well as any and all helper methods you may need.\n{template}\nThe frontend will ping the flask server you made to display data so ensure all possibilities are created by you. Also, ensure everything you do works and fits the users input. Try to limit your use of other libraries but you are allowed to import libraries. There is a file called ask-ai that contains the method ask-ai and if you need to use ai to make a prediction, you will call that method which takes a string prompt. It is similar to pinging gpt4o. Return just the code you wrote in the spot in the template and nothing else."


def gpt(prompt):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    res = completion.choices[0].message.content
    return res


def create_app(description):
    with open("../../Agents/template/app.py", "r") as f:
        template = f.read()
    res = gpt(prompt_shell(description, template))
    template = template.replace("# Write code here", res)
    return template

