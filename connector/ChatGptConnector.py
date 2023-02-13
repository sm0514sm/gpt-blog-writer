import os

import openai


class ChatGptConnector:
  def __init__(self):
    self.api_key = os.environ.get("chat_gpt_api_key")

  def create(self, model="text-davinci-003", prompt="", temperature=0.7, max_tokens=3900,
             top_p=1, frequency_penalty=0, presence_penalty=0):
    openai.api_key = self.api_key
    return openai.Completion.create(model=model,
                                    prompt=prompt,
                                    temperature=temperature,
                                    max_tokens=max_tokens,
                                    top_p=top_p,
                                    frequency_penalty=frequency_penalty,
                                    presence_penalty=presence_penalty)

  def get_one_answer(self, model="text-davinci-003", prompt="", temperature=0.5, max_tokens=3500,
                     top_p=1, frequency_penalty=0, presence_penalty=0) -> str:
    return self.create(model=model,
                       prompt=prompt,
                       temperature=temperature,
                       max_tokens=max_tokens,
                       top_p=top_p,
                       frequency_penalty=frequency_penalty,
                       presence_penalty=presence_penalty)['choices'][0]['text'].strip()


if __name__ == "__main__":
  gpt_connector = ChatGptConnector()
  topic = "Home improvement and DIY"
  test_prompt = f"Create a title related to topic {topic}, and write about it with the options below." \
                f"- Length : Length : around 3000 words" \
                f"- Format: markdown" \
                f"- Answer me in English" \
                f"- include titles" \
                f"- include subtitles and detail description" \
                f"- For audience (대상) : a person of interest in {topic}" \
                f"- Content goal (작성 목적) : blog" \
                f"- hashtags recommedation: Hashtags must always be at the end of the article, consist only of ',' and no spaces and no '#'. " \
                f"hashtags is the same format as \"#Hashtags4U: Hashtags to write\"." \
                f"you can add images to the reply by Markdown, Write the image in Markdown without backticks and without using a code block. Use the Unsplash API ([https://source.unsplash.com/1600x900/?)](https://source.unsplash.com/1600x900/?)). the query is just some tags that describes the image]" \
                f"You should add at least one image." \
                f"You can also use the bold type using the markdown. Use the word \"**word**\" in important words or sentences that are important."
  print(gpt_connector.get_one_answer(prompt=test_prompt))
