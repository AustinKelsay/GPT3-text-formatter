import json
from dotenv import load_dotenv
import openai
import os

load_dotenv()
TOKEN = os.getenv("GPT3_TOKEN")

text_prompt = "Watched Fight Club again recently, its interesting that the final mission and culmination of project mayhem is planting bombs to destroy the credit card/bank buildings totally erasing the debt record. Here we are in 2021 and we're racing towards this reality but it is our elites rather than a terrorist cult that's bringing this to fruition"


def speak(text):
  openai.api_key = TOKEN
  response = openai.Completion.create(
    engine="davinci",
    prompt=text,
    temperature=0.7,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  return response.choices[0].text

print(speak(text_prompt))