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
           f"- Length : Length : around 3500 words" \
           f"- Format: markdown" \
           f"- Answer me in English" \
           f"- include titles, subtitles and detail description" \
           f"- Content goal (작성 목적) : blog" \
           f"- hashtag consist only of ',' and no spaces and no '#' and format as \"#Hashtags4U: Hashtags to write\"." \
           f"" \
           f"you can add images to the reply by Markdown, " \
           f"Write the image in Markdown without backticks and without using a code block. " \
           f"Use the Unsplash API like this: ![?](https://source.unsplash.com/1600x900/?)" \
           f"the query is just some tags that describes the image]" \
           f"You should add at least two image!!"

  def create_post_from_topic(self, topic: Topic):
    body = self.gpt_connector.get_one_answer(prompt=self.get_prompt(topic.topic_name))
    post = Post(None, body.split("\n\n")[0], topic.topic_name, "Not started", body, "", "", "")
    self.post_repository.create_row(post)
    # TODO topic created_count 업데이트


if __name__ == "__main__":
  service = CreatePostService()
  service.create_post_from_topic(service.topic_repository.get_smallest_created_count_topic())
