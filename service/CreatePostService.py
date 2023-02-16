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
           f"- Content goal (작성 목적) : blog" \
           f"- Include title, subtitles and detail description" \
           f"- The first line should contain the title." \
           f"- The title is formatted as follows TITLE: write title here" \
           f'- Use the Unsplash API like this: <img src="https://source.unsplash.com/1600x900/?" alt="?">' \
           f'- ( After the "?", you can put a representative word from the sentence. ) ' \
           f'- The second line should contain <img>.' \
           f'- You can add additional <img> if you need to.' \
           f"- The last line should contain the hashtags." \
           f"- Hashtags are formatted as follows HASHTAG: tag1,tag2,..."

  def create_post_from_topic(self, topic: Topic):
    body = self.gpt_connector.get_one_answer(prompt=self.get_prompt(topic.topic_name))
    html_body = markdown.markdown(body)
    post = Post(
      _id=None,
      title=self.refine_title(body),
      topic=topic.topic_name,
      status="Not started",
      body='\n'.join(html_body.split("\n")[1:-1]),
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
    return body.split("\n")[0].replace("TITLE: ", "")\
      .replace("<h1>", "").replace("</h1>", "")\
      .strip()

  @staticmethod
  def refine_tags(body):
    tags = ",".join(
      body.split("HASHTAG: ")[-1].replace("#", ",").replace(".", "").replace(",,", ",").replace(" ", "")
      .replace("<h3>", "").replace("</h3>", "").replace("<p>", "").replace("</p>", "")
      .strip().split(",")
    )
    return tags[1:] if tags.startswith(",") else tags


if __name__ == "__main__":
  service = CreatePostService()
  service.create_post_from_topic(service.topic_repository.get_smallest_created_count_topic())
