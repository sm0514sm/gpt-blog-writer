from typing import List

from connector.NotionConnector import NotionConnector
from entity.notion.Post import Post


class PostRepository:
  def __init__(self):
    self.connector = NotionConnector()
    self.database_id = "c83fed76b99f4b1b8b44a003c06ffe5c"

  def find_all(self, payload) -> List[Post]:
    results = self.connector.get_all_row_from_database(self.database_id, payload)
    return [Post.map_to_post(result) for result in results]

  def create_row(self, post: Post):
    payload = Post.map_to_notion(post, self.database_id)
    self.connector.create_page(payload)

  def update_row(self, post: Post):
    payload = Post.map_to_notion(post, self.database_id)
    self.connector.update_page(post.id, payload)

  def get_oldest_post(self) -> Post:
    payload = {
      "filter": {
        "property": "status",
        "status": {
          "equals": "Not started"
        }
      },
      "sorts": [{
        "property": "created_dts",
        "direction": "ascending"
      }]
    }
    posts = self.find_all(payload)
    if not posts or len(posts) == 0:
      raise Exception("포스트가 존재하지 않음")
    return posts[0]


if __name__ == "__main__":
  post_repo = PostRepository()
  for aa in post_repo.find_all(dict()):
    print(aa)
  print(post_repo.get_oldest_post())
