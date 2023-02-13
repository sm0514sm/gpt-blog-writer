import datetime

from connector.TistoryConnector import TistoryConnector
from entity.notion.Post import Post
from entity.tistory.Category import Category
from entity.tistory.Page import Page
from repository.PostRepository import PostRepository
from repository.TopicRepository import TopicRepository


class PublishPostService:
  def __init__(self):
    self.topic_repository = TopicRepository()
    self.post_repository = PostRepository()
    self.tistory_connector = TistoryConnector()

  def publish_post(self, post: Post):
    category: Category = self.tistory_connector.get_category_by_topic_name(post.topic)
    write_page = Page(post.title, post.body, 3, category.id, "tag")
    self.tistory_connector.write(write_page)

    # 정상적으로 발행이 되면

    post.status = "Published"
    post.published_dts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    self.post_repository.update_row(post)

    topic = self.topic_repository.find_by_topic_name(post.topic)
    topic.published_count += 1
    self.topic_repository.update_row(topic)


if __name__ == "__main__":
  service = PublishPostService()
  service.publish_post(PostRepository().get_oldest_post())
