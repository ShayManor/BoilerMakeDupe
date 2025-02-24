from enum import Enum


class AI(Enum):
    CHATGPT = 'GPT.py'
    CLAUDE = 'GPT.py'
    DEEPSEEK = 'DeepSeek.py'
    GEMINI = 'Gemini.py'


class ASSISTANTS(Enum):
    BASH_CREATOR = 'asst_nLZzDR6BjhI74Vu6Ep7PN5lz'
    APP_LIST_METHODS = ''
    APP_FILL_METHODS = ''


class AGENT:
    name = ''
    description = ''
    model = AI.CHATGPT
    path = "../../Agents"
