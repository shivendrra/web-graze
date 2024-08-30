import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import os
import logging
import timeit

logging.basicConfig(filename="wiki_scraper.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def build_urls(query):
  new_query = "_".join(query.split(" "))
  wiki_url = f"https://en.wikipedia.org/wiki/{new_query}"
  return wiki_url

def scrapper(urls, headers):
  noUrl = 0
  r = requests.get(urls, headers=headers)
  if r.status_code == 200:
    soup = bs(r.content, "html.parser")
    paragraphs = soup.find_all("p")
    noUrl += 1
    return paragraphs, noUrl
  else:
    logging.error(f"Failed to fetch the URL: {urls}. Status code: {r.status_code}")
    return None, 0

def fetch_extra_urls(query, headers):
  urls = []
  new_query = "_".join(query.split(" "))
  wiki_url = f"https://en.wikipedia.org/wiki/{new_query}"

  r = requests.get(wiki_url, headers=headers)
  if r.status_code == 200:
    soup = bs(r.content, "html.parser")
    links = soup.find_all("a")
    urls.extend([url.get("href") for url in links])
  else:
    logging.error(f"Failed to fetch the URL: {wiki_url}. Status code: {r.status_code}")

  return urls  

def extra_scrape(url, headers):
  noUrl = 0
  if url.startswith("/"):
    target_url = f"https://en.wikipedia.org{url}"
    r = requests.get(target_url, headers=headers)
  else:
    return None, 0
  if r.status_code == 200:
    soup = bs(r.content, "html.parser")
    paragraphs = soup.find_all("p")
    noUrl += 1
    return paragraphs, noUrl
  else:
    logging.error(f"Failed to fetch the URL: {target_url}. Status code: {r.status_code}")
    return None, 0

class Wikipedia:
  def __init__(self, filepath: str, metrics: bool = False) -> None:
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    self.directory, filename_with_ext = os.path.split(filepath)
    self.filename, ext = os.path.splitext(filename_with_ext)
    self.filename = self.filename.strip()
    if not os.path.exists(self.directory):
      os.makedirs(self.directory)
    self.metrics = metrics
    self.list_urls = []
    self.extra_urls = []
    self.total_time = 0
    self.fetched_urls = 0

  def __call__(self, queries: list[str], extra_urls: bool = False):
    if not queries:
      raise ValueError("Queries can't be empty, add some!")
    else:
      start_time = timeit.default_timer()
      for query in tqdm(queries, desc="Generating Valid Target Urls"):
        target_url = build_urls(query)
        self.list_urls.append(target_url)

      for url in tqdm(self.list_urls, desc="Scraping the web-pages"):
        out_page, noUrl1 = scrapper(url, self.headers)
        if out_page is not None:
          self.write_to_file(out_page)
        self.fetched_urls += noUrl1

      if extra_urls:
        for query in queries:
          extra_urls = fetch_extra_urls(query, self.headers)
          for url in extra_urls:
            extra_content, noUrl2 = extra_scrape(url, self.headers)
            if extra_content is not None:
              self.write_to_file(extra_content)
          self.fetched_urls += noUrl2
    
    end_time = timeit.default_timer()
    self.total_time = end_time - start_time
    if self.metrics:
      self.get_metrics()

  def write_to_file(self, paragraphs):
    filepath = os.path.join(self.directory, f"{self.filename}.txt")
    with open(filepath, "a", encoding="utf-8") as f:
      for paragraph in paragraphs:
        text = paragraph.get_text()
        f.write(text + "\n")

  def get_metrics(self):
    if self.total_time < 60:
      time_display = f"{self.total_time:.2f} secs"
    elif self.total_time < 3600:
      time_display = f"{self.total_time / 60:.2f} mins"
    else:
      time_display = f"{self.total_time / 3600:.2f} hours"
      
    print("\n")
    print("Wikipedia scraping metrics:\n")
    print("------------------------------------------------------")
    print(f"Total URL's fetched: {len(self.list_urls) + len(self.extra_urls)}")
    print(f"Total URLs processed: {self.fetched_urls}")
    print(f"Total time taken: {time_display}")
    print("------------------------------------------------------")