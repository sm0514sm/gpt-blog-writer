from typing import List

from connector.NotionConnector import NotionConnector
from entity.notion.Post import Post


class PostRepository:
  def __init__(self):
    self.connector = NotionConnector()
    self.database_id = "c83fed76b99f4b1b8b44a003c06ffe5c"

  def find_all(self) -> List[Post]:
    results = self.connector.get_all_row_from_database(self.database_id, dict())
    return [Post.map_to_post(result) for result in results]

  def create_row(self, post: Post):
    payload = Post.map_to_notion(post, self.database_id)
    self.connector.create_page(payload)

  def update_row(self, post: Post):
    payload = Post.map_to_notion(post, self.database_id)
    self.connector.update_page(post.id, payload)


if __name__ == "__main__":
  posts = PostRepository()
  for aa in posts.find_all():
    aa.id = None
    posts.create_row(aa)
