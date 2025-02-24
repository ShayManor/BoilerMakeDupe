import google.generativeai as genai


def ask_ai(prompt: str):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    print(response.text)
