import datetime
import os

from requests import get


class NaverApiConnector:
  def __init__(self):
    self.hdr = {
      "X-Naver-Client-Id": os.environ.get("X-NAVER-CLIENT-ID"),
      "X-Naver-Client-Secret": os.environ.get("X-NAVER-CLIENT-SECRET")
    }

  def _get_response(self, keyword: str) -> dict:
    url = f"https://openapi.naver.com/v1/search/news.json?query={keyword}&display=50"
    return get(url, headers=self.hdr).json()

  def get_best_one_news(self, keyword: str) -> str | None:
    response = self._get_response(keyword)
    result_items: list[dict] = []
    items: list[dict] = response.get("items")
    items = list(filter(lambda v: "n.news.naver.com" in v["link"], items))
    for item in items:
      pub_date = datetime.datetime.strptime(item['pubDate'][:-6], "%a, %d %b %Y %H:%M:%S")
      if datetime.datetime.now() <= datetime.timedelta(days=7) + pub_date:
        result_items.append(item)
    if not result_items:
      return
    for result_item in result_items:
      if keyword in result_item["title"]:
        return result_item['link']
    return result_items[0]['link']


if __name__ == "__main__":
  connector = NaverApiConnector()
  print(connector.get_best_one_news("대정령"))
