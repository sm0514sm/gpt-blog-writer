import datetime


class Post:
  def __init__(self, _id, title, topic, status, body, created_dts, published_dts, post_id, tags):
    self.id: str = _id
    self.title: str = title
    self.topic: str = topic
    self.status: str = status
    self.body: str = body
    self.created_dts: str = created_dts
    self.published_dts: str = published_dts
    self.post_id: str = post_id
    self.tags: str = tags

  def __str__(self):
    return f"Post={{{self.id=}, {self.title=}, {self.topic=}, " \
           f"{self.status=}, {self.created_dts}, {self.published_dts}, {self.tags}}}"

  @staticmethod
  def map_to_post(result):
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
      tags=properties['tags']['rich_text'][0]['text']['content'] if properties['tags']['rich_text'] else "",
    )

  def map_to_notion(self, database_id) -> dict:
    return {
      "parent": {
        "type": "database_id",
        "database_id": database_id
      },
      "properties": {
        "title": {"title": [{"text": {"content": self.title}}]},
        "topic": {"select": {"name": self.topic}},
        "status": {"status": {"name": self.status}},
        "body": {"rich_text": self.make_long_rich_text(self.body)},
        "published_dts": {"date": {"start": self.published_dts}},
        "post_id": {"rich_text": [{"text": {"content": self.post_id}}]},
        "tags": {"rich_text": [{"text": {"content": self.tags}}]}
      }
    }

  @staticmethod
  def make_long_rich_text(body):
    return [{"text": {"content": i}} for i in split_string(body, 2000)]


def split_string(string, chunk_size) -> list:
  return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]
