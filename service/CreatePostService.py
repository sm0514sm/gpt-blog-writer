import markdown

from connector.ChatGptConnector import ChatGptConnector
from entity.notion.Post import Post
from entity.notion.Topic import Topic
from repository.PostRepository import PostRepository
from repository.TopicRepository import TopicRepository


class CreatePostService:
  def __init__(self):
    self.gpt_connector = ChatGptConnector()
    self.topic_repository = TopicRepository()
    self.post_repository = PostRepository()

  @staticmethod
  def get_prompt(topic_name):
    return f"Create a title related to topic \"{topic_name}\", and write about it with the options below." \
           f"- Length : Length : around 3000 words" \
           f"- Format: html" \
           f"- Answer me in English" \
           f"- include titles, subtitles and detail description" \
           f"- Content goal (작성 목적) : blog" \
           f"- hashtag consist only of ',' and no spaces and no '#' and format as \"###Hashtags4U: Hashtags to write\"." \
           f"" \
           f"you can add images to the reply by html tags, " \
           f"Write the image in html without using a code block. " \
           f'Use the Unsplash API like this: <img src="https://source.unsplash.com/1600x900/?" alt="?">' \
           f"the query is just some tags that describes the image" \
           f"You should add at least two image!!" \
           f"Put the image tag in the middle of the sentence."

  def create_post_from_topic(self, topic: Topic):
    body = self.gpt_connector.get_one_answer(prompt=self.get_prompt(topic.topic_name))
    html_body = markdown.markdown(body)
    post = Post(
      _id=None,
      title=self.refine_title(body),
      topic=topic.topic_name,
      status="Not started",
      body=html_body,
      post_id="",
      created_dts="",
      published_dts="",
      tags=self.refine_tags(body)
    )
    self.post_repository.create_row(post)
    # 성공하면
    topic.created_count += 1
    self.topic_repository.update_row(topic)

  @staticmethod
  def refine_title(body):
    return body.split("\n\n")[0].replace("#", "")\
      .replace("<h1>", "").replace("</h1>", "")\
      .strip()

  @staticmethod
  def refine_tags(body):
    return ",".join(
      body.split("Hashtags4U: ")[-1].replace("#", "").replace(".", "").replace("Hashtags4U: ", "").replace(" ", "")
      .replace("<h3>", "").replace("</h3>", "")
      .strip().split(",")
    )


if __name__ == "__main__":
  service = CreatePostService()
  service.create_post_from_topic(service.topic_repository.get_smallest_created_count_topic())
