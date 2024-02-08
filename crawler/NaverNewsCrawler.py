import requests
from bs4 import BeautifulSoup


def get_article_body(url: str) -> str:
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  article_body = soup.find("div", id="articeBody")
  if not article_body:
    return soup.find("article", id="dic_area").text
  return article_body.text


def get_clean_article_body(url) -> str:
  return (get_article_body(url)
          .replace("[서울=뉴시스]", "")
          .replace("tubeguide@newsis.com", "")
          .replace("▶기사문의/제보 :", "")
          .replace("◎튜브가이드▶홈페이지 : ", "")
          .replace("*재판매 및 DB 금지", "")
          .replace("photo@newsis.com ", "")
          .replace('\n', '')
          .strip())


if __name__ == '__main__':
  print(get_clean_article_body('https://n.news.naver.com/mnews/article/092/0002320840?sid=105'))
