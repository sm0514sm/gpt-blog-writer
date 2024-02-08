from typing import List

import requests

base_url = "https://namu.wiki"


def get_best_keyword() -> List:
  url = "https://search.namu.wiki/api/ranking"
  response = requests.get(url)
  data = response.json()
  return data


if __name__ == "__main__":
  print(get_best_keyword())
