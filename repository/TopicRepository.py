from typing import List

from connector.NotionConnector import NotionConnector
from entity.notion.Topic import Topic


class TopicRepository:
  def __init__(self):
    self.connector = NotionConnector()
    self.database_id = "57120f6893604b61b8bb4ba3ccd44533"

  def find_all(self) -> List[Topic]:
    results = self.connector.get_all_row_from_database(self.database_id, dict())
    return [self.map_to_image_database_row(result) for result in results]

  def update_row(self, row: Topic):
    payload = {
      "properties": {
        "published_count": {"number": int(row.published_count)},
        "created_count": {"number": int(row.created_count)},
        "use": {"checkbox": row.use},
      }}
    self.connector.update_page(row.id, payload)

  @staticmethod
  def map_to_image_database_row(result) -> Topic:
    properties = result['properties']

    return Topic(
      _id=result['id'],
      use=properties['use']['checkbox'],
      topic_name=properties['topic_name']['title'][0]['plain_text'].strip(),
      published_count=0 if properties['published_count']['number'] is None else properties['published_count']['number'],
      created_count=0 if properties['created_count']['number'] is None else properties['created_count']['number'],
    )

  def get_smallest_created_count_topic(self) -> Topic:
    self.find_all()
    # TODO 뭐 use로 필터를 해야함
    # TODO 뭐 count 순으로 오름차순 정렬을 해야함
    # TODO return 가장 작은 수의 토픽


if __name__ == "__main__":
  topics = TopicRepository()
  for i in topics.find_all():
    print(i)
