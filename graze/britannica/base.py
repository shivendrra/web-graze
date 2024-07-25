import requests
from bs4 import BeautifulSoup
import time
class BritannicaUrls:
  def __init__(self, search_queries, max_limit):
    self.max_limit = max_limit
    self.search_queries = search_queries
    self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

  def build_url(self, query, pageNo):
    formattedQuery = '%20'.join(query.split(' '))
    url = f"https://www.britannica.com/search?query={formattedQuery}&page={pageNo}"
    return url

  def get_target_url(self, target_url):
    while True:
      r = requests.get(target_url, headers=self.headers)
      if r.status_code == 200:
        html_content = r.content
        soup = BeautifulSoup(html_content, 'html.parser')
        fetched_urls = soup.find_all('a', class_='md-crosslink')
        list_url = [url.get('href') for url in fetched_urls]
        return list_url
      
      elif r.status_code == 429:
        print(f"Rate limit exceeded. Waiting 30secs before retrying: {target_url}")
        time.sleep(30)
      else:
        print(f"Skipping this URL due to status code {r.status_code}: {target_url}")
        return []

  def generate_urls(self, progress_bar=None):
    page_urls = []
    current_iteration = 0

    for query in self.search_queries:
      pageNo = 1
      for i in range(self.max_limit):
        target_url = self.build_url(query, pageNo)
        pageNo += 1
        new_url = self.get_target_url(target_url)
        if new_url:
          page_urls.extend(new_url)
        current_iteration += 1
        if progress_bar:
          progress_bar.update(1)
    return page_urls