import json
import openai

with open('secrets.json') as f:
  obj = json.load(f)
  value = json.dumps(obj)
  token = value[16:59]

openai.api_key = token

response = openai.Completion.create(
  engine="davinci",
  prompt="Division of labor. It is not immediately intuitive that specializing rather than generalizing would increase productivity, but because the fact that humans are innovators those that specialize also innovate their craft and leverage insight to increase their production. Therefore a society that specializes, advances significantly. Now in the scenario of specialization what is absolutely required is a unit of money or value or proof of work to allow exchange between all of the specialist individual‘s.",
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)

