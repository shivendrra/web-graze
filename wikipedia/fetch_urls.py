import os
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

class WikiURLScraper:
  def __init__(self):
    self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    self.total_urls = 0

  def scrape_from_file(self, url_file, out_file):
    with open(url_file, 'r') as f:
      urls = f.readlines()
        
    for url in tqdm(urls, desc="Scrapping the web-pages"):
      out_page = self.scrapper(url.strip())
      with open(out_file, 'a', encoding='utf-8') as outfile:
        if out_page is not None:
          for paragraph in out_page:
            text = paragraph.get_text()
            outfile.write(text)
        else:
          continue
        
    print(f'Total fetched URLs: {self.total_urls}')

  def scrapper(self, url):
    r = requests.get(url, headers=self.headers)
    if r.status_code == 200:
      soup = bs(r.content, 'html.parser')
      paragraphs = soup.find_all('p')
      self.total_urls += 1
      return paragraphs
    else:
      pass