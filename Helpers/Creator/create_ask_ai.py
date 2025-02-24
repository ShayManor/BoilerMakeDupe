
def create_ask_ai(AI):
    with open(f'Ask_AI-Options/{AI.value}', 'r') as f:
        return f.read()
