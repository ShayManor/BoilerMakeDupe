from openai import OpenAI


def prompt_shell(desc, app):
    return f"You are a professional html developer who will take a flask server and a description of what it should do and create a clean and modern html frontend to accomplish all of the goals. Don't ever use localhost or any ip, just use /endpoint. You will ping the flask server with the ip localhost:5000 when you need data and you will make the frontend good. Only return the html code with nothing else. You will make this look good and be relevant to the description, for example a bread store could have different clipart pictures of bread on the page. Make this look good and professional. Focus on the user experience and make sure everything makes sense.The app you will create is: {desc}. Here is the flask server: {app}"


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


def create_index(description, app):
    res = gpt(prompt_shell(description, app))
    return res
