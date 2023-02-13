from typing import List

from connector.TistoryConnector import TistoryConnector
from entity.tistory.Category import Category


class PageRepository:
  def __init__(self):
    self.connector = TistoryConnector()

  def get_categories(self) -> List[Category]:
    return [Category.map_to_category(category) for category in self.connector.get_category_list()]

  def get_category_by_topic_name(self, topic_name):
    for category in self.get_categories():
      if category.name == topic_name:
        return category


if __name__ == "__main__":
  pass
