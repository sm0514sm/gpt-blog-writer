import json
import os

from requests import post, patch, get


class NotionConnector:
  def __init__(self):
    self.token = os.environ.get("NOTION_TOKEN")
    self.hdr = {
      "Authorization": f"Bearer {self.token}",
      "Notion-Version": "2021-08-16",
      "Content-Type": "application/json"
    }

  def get_all_row_from_database(self, database_id, extra_data: dict):
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    datas: dict = extra_data
    result_list = []
    while True:
      result_dict = post(url, headers=self.hdr, json=datas).json()
      print(result_dict)
      print(self.token)
      result_list += result_dict['results']

      if not result_dict['has_more']:
        break
      datas['start_cursor'] = result_dict['next_cursor']
    return result_list

  def create_page(self, payload):
    url = f'https://api.notion.com/v1/pages'
    reseponse = post(url, headers=self.hdr, data=json.dumps(payload))
    print(f"create_page: {reseponse.json()}")

  def update_page(self, page_id, payload):
    url = f'https://api.notion.com/v1/pages/{page_id}'
    reseponse = patch(url, headers=self.hdr, data=json.dumps(payload))
    print(f"update_page: {reseponse.json()}")

  def get_page(self, page_id):
    url = f'https://api.notion.com/v1/pages/{page_id}'
    reseponse = get(url, headers=self.hdr)
    print(f"get_page: {reseponse.json()}")


if __name__ == "__main__":
  database = NotionConnector().get_all_row_from_database("57120f6893604b61b8bb4ba3ccd44533", dict())
  print(len(database))
  NotionConnector().get_page("ce741f77-6539-408b-91a6-bbbe0cbf7925")
