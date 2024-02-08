import os

import openai
from openai import OpenAI
from openai.types.chat import ChatCompletion


class ChatGptConnector:
  def __init__(self, model: str = "gpt-3.5-turbo-16k", role: str = "You are a helpful assistant."):
    self.api_key = os.environ.get("OPEN-AI-API-SECRET")
    self.client = OpenAI(organization='org-bGbR7ff5ICz9MIqSZ4aQLqwr', api_key=self.api_key)
    self.model = model
    self.role = role

  def get(self, article: str) -> str:
    create: ChatCompletion = self.client.chat.completions.create(model=self.model, max_tokens=6157,
                                                                 messages=[{"role": "system", "content": self.role},
                                                                           {"role": "user", "content": article}, ])
    return create.choices[0].message.content

  def create(self, model="gpt-3.5-turbo-0125", prompt="", temperature=0.7, max_tokens=3900,
             top_p=0.7, frequency_penalty=0.1, presence_penalty=0.3):
    openai.api_key = self.api_key
    return openai.Completion.create(model=model,
                                    prompt=prompt,
                                    temperature=temperature,
                                    max_tokens=max_tokens,
                                    top_p=top_p,
                                    frequency_penalty=frequency_penalty,
                                    presence_penalty=presence_penalty)

  def get_one_answer(self, model="text-davinci-003", prompt="", temperature=0.5, max_tokens=3800,
                     top_p=0.7, frequency_penalty=0.1, presence_penalty=0) -> str:
    return self.create(model=model,
                       prompt=prompt,
                       temperature=temperature,
                       max_tokens=max_tokens,
                       top_p=top_p,
                       frequency_penalty=frequency_penalty,
                       presence_penalty=presence_penalty)['choices'][0]['text'].strip()


if __name__ == "__main__":
  gpt_connector = ChatGptConnector()
  print(gpt_connector.get("안뇽"))
