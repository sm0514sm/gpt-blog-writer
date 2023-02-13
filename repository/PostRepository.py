import datetime
from typing import List

from connector.NotionConnector import NotionConnector
from entity.notion.Post import Post


class PostRepository:
  def __init__(self):
    self.connector = NotionConnector()
    self.database_id = "c83fed76b99f4b1b8b44a003c06ffe5c"

  def find_all(self) -> List[Post]:
    results = self.connector.get_all_row_from_database(self.database_id, dict())
    return [self.map_to_post(result) for result in results]

  def create_row(self, post: Post):
    payload = self.map_to_notion(post)
    self.connector.create_page(payload)

  def update_row(self, post: Post):
    payload = self.map_to_notion(post)
    self.connector.update_page(post.id, payload)

  @staticmethod
  def map_to_post(result) -> Post:
    properties = result['properties']

    return Post(
      _id=result['id'],
      title=properties['title']['title'][0]['plain_text'].strip(),
      topic=properties['topic']['select']['name'],
      status=properties['status']['status']['name'],
      body=properties['body']['rich_text'][0]['plain_text'] if properties['body']['rich_text'] else "",
      created_dts=properties['created_dts']['created_time'],
      published_dts=properties['published_dts']['date'],
      post_id=properties['post_id']['rich_text'][0]['text']['content'],
    )

  def map_to_notion(self, post: Post) -> dict:
    return {
      "parent": {
        "type": "database_id",
        "database_id": self.database_id
      },
      "properties": {
        "title": {"title": [{"text": {"content": post.title}}]},
        "topic": {"select": {"name": post.topic}},
        "status": {"status": {"name": post.status}},
        "body": {"rich_text": self.make_long_rich_text(post.body)},
        "published_dts": {"date": {"start": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")}},
        "post_id": {"rich_text": [{"text": {"content": post.post_id}}]}
      }
    }

  @staticmethod
  def make_long_rich_text(body):
    return [{"text": {"content": i}} for i in split_string(body, 2000)]


def split_string(string, chunk_size) -> list:
  return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]


if __name__ == "__main__":
  posts = PostRepository()
  for aa in posts.find_all():
    aa.id = None
    posts.create_row(aa)
