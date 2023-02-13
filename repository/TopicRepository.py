from typing import List

from connector.NotionConnector import NotionConnector
from entity.notion.Topic import Topic


class TopicRepository:
  def __init__(self):
    self.connector = NotionConnector()
    self.database_id = "57120f6893604b61b8bb4ba3ccd44533"

  def find_all(self, payload) -> List[Topic]:
    results = self.connector.get_all_row_from_database(self.database_id, payload)
    return [Topic.map_to_topic(result) for result in results]

  def update_row(self, row: Topic):
    self.connector.update_page(row.id, row.map_to_notion())

  def find_by_topic_name(self, topic_name) -> Topic:
    for topic in self.find_all(dict()):
      if topic.topic_name == topic_name:
        return topic

  def get_smallest_created_count_topic(self) -> Topic:
    payload = {
      "filter": {
        "property": "use",
        "checkbox": {
          "equals": True
        }
      },
      "sorts": [{
        "property": "created_count",
        "direction": "ascending"
      }]
    }
    topics = self.find_all(payload)
    if not topics or len(topics) == 0:
      raise Exception("토픽이 존재하지 않음")
    return topics[0]

  def increate_created_count(self, topic) -> None:
    self.connector.update_page(topic.id, dict())


if __name__ == "__main__":
  topicRepo = TopicRepository()
  print(topicRepo.get_smallest_created_count_topic())
