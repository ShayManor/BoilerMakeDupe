from openai import OpenAI

def gpt(app):
    client = OpenAI()
    assistant_id = "asst_nLZzDR6BjhI74Vu6Ep7PN5lz"
    assistant = client.beta.assistants.retrieve(
        assistant_id=assistant_id
    )
    thread = client.beta.threads.create(
        messages=[{"role": "user", "content": app}]
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        ai_response = messages.data[0].content[0].text.value
        return ai_response


def create_run(app: str):
    return gpt(app)
