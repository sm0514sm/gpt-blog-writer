from connector.ChatGptConnector import ChatGptConnector
from connector.NaverApiConnector import NaverApiConnector
from crawler import NaverNewsCrawler
from entity.tistory.Page import Page
from service import RequestBestKeywords

role_prompt = """
    당신은 사용자로부터 입력된 내용을 완성된 블로그 글로 작성해주는 도구입니다.
    꼼꼼히 생각해서 어떻게 하면 더욱 진짜 블로그 글과 유사할지 고민하고 천천히 작성해주세요.
    아래 조건을 반드시 준수하고 사용자가 입력한 내용을 블로그 글과 같이 작성해주세요.
    - 콘텐츠의 목적은 "블로그 글 작성"
    - 항상 존대말로 작성
    - 포맷은 html로 작성
    - 날짜가 있을 경우에 가장 최신인 2024년 2월에 관련된 내용에 집중해주세요
    - 6000자 내외로 작성
    - 맨 첫줄은 제목을 작성하고 소주제와 내용을 구분 필요
    - 제목은 seo에 잘맞고 20~30대 청년들이 흥미를 가지도록 설정
    - Unsplash API를 사용해서 이미지 삽입
    - like this: <img src="https://source.unsplash.com/1600x900/?" alt="?"> ( After the "?", you can put a representative word from the sentence. )
    - 기사 제목과 기자 이름, 이메일 주소와 출처 등은 반드시 삭제
    """


class CreateNewsConvertService:
  def __init__(self):
    self.chat_gpt_connector = ChatGptConnector(model="gpt-4-0613", role=role_prompt)
    self.naver_api_connector = NaverApiConnector()
    self.best_keywords: list = RequestBestKeywords.get_best_keyword()
    print(self.best_keywords)

  def create_page(self) -> Page | None:
    link = self.naver_api_connector.get_best_one_news(self.best_keywords[9])
    print(f"link: {link}")
    if link is None:
      print("keyword link is None")
      return
    article_body = NaverNewsCrawler.get_clean_article_body(link)
    print(f"article_body: {article_body}")
    result = self.chat_gpt_connector.get(article_body)
    print(f"result: {result}")


if __name__ == "__main__":
  service = CreateNewsConvertService()
  service.create_page()
