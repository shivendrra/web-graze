import os
import logging
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import timeit, time
import re

logging.basicConfig(filename="britannica_scraper.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

def build_britannica_url(query, page_no):
  formatted_query = '%20'.join(query.split(' '))
  url = f"https://www.britannica.com/search?query={formatted_query}&page={page_no}"
  return url

def get_target_url(target_url, headers):
  while True:
    r = requests.get(target_url, headers=headers)
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

class Britannica:
  def __init__(self, filepath:str, max_limit:int=10, metrics:bool=False) -> None:
    self.directory, filename_with_ext = os.path.split(filepath)
    self.filename, ext = os.path.splitext(filename_with_ext)
    self.filename = self.filename.strip()
    if not os.path.exists(self.directory):
      os.makedirs(self.directory)
    self.max_limit = max_limit
    self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    self.metrics = metrics
    self.total_urls = 0
    self.total_pages = 0

  def __call__(self, queries:list[str]):
    if not queries:
      raise ValueError("Search queries can't be empty.")
    else:
      self.total_time = timeit.default_timer()
      for query in tqdm(queries, desc="Generating Britannica URLs"):
        page_no = 1
        for i in range(self.max_limit):
          target_url = build_britannica_url(query, page_no)
          new_urls = get_target_url(target_url, self.headers)
          if new_urls:
            self.write_urls_to_file(new_urls)
            self.total_urls += len(new_urls)
          page_no += 1
      
      self.total_time = timeit.default_timer() - self.total_time
      if self.metrics:
        self.get_metrics()

  def text_extractor(self, url_snippet):
    target_url = f"https://britannica.com{url_snippet}"
    r = requests.get(target_url, headers=self.headers)

    if r.status_code == 200:
      soup = BeautifulSoup(r.content, 'html.parser')
      paragraphs = soup.find_all('p')
      page = '\n'.join([p.get_text() for p in paragraphs if "Our editors will review what you’ve submitted and determine whether to revise the article." not in p.get_text()])
      page = re.sub('&\w+;', '', page)
      self.total_pages += 1
      return page
    else:
      print(f"Failed to fetch page content: {target_url}")
      return None

  def write_urls_to_file(self, url_snippets):
    filepath = os.path.join(self.directory, f"{self.filename}.txt")
    with open(filepath, 'a', encoding='utf-8') as f:
      for snippet in url_snippets:
        page = self.text_extractor(snippet)
        if page:
          f.write(page)
          f.write("\n")

  def get_metrics(self):
    print("\n")
    print("Britannica scraping metrics:\n")
    print("------------------------------------------------------")
    print(f"Total URLs fetched: {self.total_urls}")
    print(f"Total pages extracted: {self.total_pages}")
    if self.total_time < 60:
      print(f"Total time taken: {self.total_time:.2f} seconds")
    elif self.total_time < 3600:
      print(f"Total time taken: {self.total_time/60:.2f} minutes")
    else:
      print(f"Total time taken: {self.total_time/3600:.2f} hours")
    print("------------------------------------------------------")