"""
  --> generates a target wikipeida-url from the provided queries
  --> sends a request to that url and fetches the comeplete webpage
  --> writes it in a file
"""

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

class WikiScraper:
  def __init__(self):
    self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    self.list_urls = []

  def __call__(self, search_queries, out_file=None):
    if out_file is not None:
      for query in tqdm(search_queries, desc="Generating valid urls"):
        target_url = self.build_urls(query)
        self.list_urls.append(target_url)
      
      for url in tqdm(self.list_urls, desc="Scrapping the web-pages\t"):
        out_page = self.scrapper(url)
        with open(out_file, 'a', encoding='utf-8') as f:
          for paragraph in out_page:
            text = paragraph.get_text()
            f.write(text)
    else:
      raise ValueError('provide a output file')
  
  def build_urls(self, query):
    new_query = '_'.join(query.split(' '))
    wiki_url = f"https://en.wikipedia.org/wiki/{new_query}"
    return wiki_url
  
  def scrapper(self, urls):
    r = requests.get(urls, headers=self.headers)
    if r.status_code == 200:
      soup = bs(r.content, 'html.parser')
      paragraphs = soup.find_all('p')

      return paragraphs
    else:
      pass