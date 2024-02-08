from typing import List

import requests
from bs4 import BeautifulSoup

base_url = "https://namu.wiki"


def get_best_keyword() -> List:
  url = base_url + "/api/ranking"
  response = requests.get(url)
  data = response.json()
  return data


def get_html(keyword: str) -> str:
  response = requests.get(base_url + "/w/" + keyword)
  html = response.content
  soup = BeautifulSoup(html, 'html.parser')
  elements = soup.select('a')
  for element in elements:
    url = element.get('href')
    if "history" in url:
      return base_url + url


print(get_html("손흥민"))
