import json
from dotenv import load_dotenv
import openai
import os

load_dotenv()
TOKEN = os.getenv("GPT3_TOKEN")


openai.api_key = TOKEN


start_chat_log = '''World: Say something clever about the stock market.
AI: In the markets those that develop an independent point of view outpreform the crowd.
World: Say something funny about evolution.
AI: Biology is the only science in which multiplication means the same thing as division.
World: Say something interesting about the human mind.
AI: The mind is a tool for thinking, the brain is a tool for survival.
'''

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}World: {question}\nAI: {answer}\n'


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}World: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nWorld'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer
