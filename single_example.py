import json
import openai

with open('secrets.json') as f:
  obj = json.load(f)
  value = json.dumps(obj)
  token = value[16:59]

text_prompt = "Watched Fight Club again recently, its interesting that the final mission and culmination of project mayhem is planting bombs to destroy the credit card/bank buildings totally erasing the debt record. Here we are in 2021 and we're racing towards this reality but it is our elites rather than a terrorist cult that's bringing this to fruition"

openai.api_key = token

response = openai.Completion.create(
  engine="davinci",
  prompt=text_prompt,
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)

