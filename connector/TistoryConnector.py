import json
import os

from requests import get, post

from entity.tistory.Category import Category
from entity.tistory.Page import Page


class TistoryConnector:
  def __init__(self):
    self.access_token = os.environ.get("tistory_access_token")
    self.blogName = "lifaon"

  def get_categories(self) -> list[Category]:
    url = "https://www.tistory.com/apis/category/list"
    params = {'access_token': self.access_token, "output": "json", "blogName": "lifaon"}
    response = get(url, params=params)
    if not response or response.status_code != 200:
      return []
    return [Category.map_to_category(category) for category in response.json()['tistory']['item']['categories']]

  def get_category_by_topic_name(self, topic_name):
    for category in self.get_categories():
      if category.name == topic_name:
        return category

  def write(self, write_page: Page):
    url = f'https://www.tistory.com/apis/post/write'
    payload = {
      "access_token": self.access_token,
      "blogName": self.blogName,
      "title": write_page.title,
      "content": write_page.content,
      "visibility": write_page.visibility,
      "category": write_page.category,
      "tag": write_page.tag
    }
    reseponse = post(url, data=json.dumps(payload))
    return reseponse.status_code


if __name__ == "__main__":
  connector = TistoryConnector()
  print(connector.get_categories())
