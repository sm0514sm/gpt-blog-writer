import re
import time
from datetime import datetime, timedelta
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By

from entity.Crawl.Revision import Revision

now = datetime.now()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('headless')
user_agent = ("Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/71.0.3578.83 Mobile Safari/537.36")
options.add_argument('user-agent=' + user_agent)
driver = webdriver.Chrome(options=options)

driver.get("https://namu.wiki/history/%EC%86%90%ED%9D%A5%EB%AF%BC")
driver.implicitly_wait(2)
li_list = driver.find_elements(By.TAG_NAME, 'li')[:30]
revision_list: List[Revision] = []
for li in li_list:
  revision_number = int(li.find_element(By.TAG_NAME, "strong").text[1:])
  update_datetime = datetime.strptime(li.find_element(By.TAG_NAME, "time").text, '%Y-%m-%d %H:%M:%S')
  revision_list.append(Revision(update_datetime, revision_number))
for revision in revision_list:
  if now - revision.update_datetime > timedelta(hours=24):
    continue
  time.sleep(5)
  driver.get(
    f"https://namu.wiki/diff/%EC%86%90%ED%9D%A5%EB%AF%BC?rev={revision.number}&oldrev={revision.number - 1}")
  driver.implicitly_wait(2)
  elements = driver.find_elements(By.TAG_NAME, 'td')
  for e in elements:
    if e.get_attribute("class") != "insert":
      continue
    cleantext = re.sub(r'\||include\(|\[|]|틀|\'|<|>|\{|}|inline|padding|margin|border-radius', '', e.text).strip()
    print(cleantext)
driver.quit()
