import os

from requests import get


class TistoryConnector:
  def __init__(self):
    self.access_token = os.environ.get("tistory_access_token")
    self.blogName = "lifaon"

  def get_category_list(self):
    url = "https://www.tistory.com/apis/category/list"
    params = {'access_token': self.access_token, "output": "json", "blogName": "lifaon"}
    response = get(url, params=params)
    print(response.json()['tistory']['item']['categories'])


if __name__ == "__main__":
  connector = TistoryConnector()
  connector.get_category_list()
