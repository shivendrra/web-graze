import os, logging, requests, timeit, time, re, random
from bs4 import BeautifulSoup
from tqdm import tqdm
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

def build_search_url(query, page_no):
  formatted_query = '%20'.join(query.split(' '))
  url = f"https://www.britannica.com/search?query={formatted_query}&page={page_no}"
  return url

class Britannica:
  USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
  ]

  def __init__(self, filepath: str, max_pages: int = 10, metrics: bool = False, max_workers: int = 3, delay: float = 1.0):
    self.directory, filename_with_ext = os.path.split(filepath)
    self.filename = os.path.splitext(filename_with_ext)[0].strip()
    self.max_pages, self.metrics, self.max_workers, self.delay = max_pages, metrics, max_workers, delay
    self.total_urls, self.total_pages, self.total_time = 0, 0, 0
    self.BASE_URL = "https://www.britannica.com"  # Added missing BASE_URL
    os.makedirs(self.directory, exist_ok=True)

    self.session = requests.Session()
    self.session.headers.update({
      'User-Agent': random.choice(self.USER_AGENTS),
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate',
      'Referer': 'https://www.google.com/',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
    })

    self.logger = logging.getLogger(__name__)
    handler = logging.FileHandler("../britannica_scraper.log")
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    self.logger.addHandler(handler)
    self.logger.setLevel(logging.INFO)
    self.logger.info("Britannica scraper initialized")

  def _extract_article_urls(self, response: requests.Response) -> List[str]:
    try:
      soup = BeautifulSoup(response.content, 'html.parser')
      selectors, urls, unique_urls = ['a[href*="/topic/"]', 'a[href*="/biography/"]', 'a[href*="/place/"]', 'a[href*="/event/"]', '.result-title a', '.search-result a', 'h3 a', 'a.md-crosslink'], [], []
      for selector in selectors:
        links = soup.select(selector)
        if links:
          for link in links:
            href = link.get('href')
            if href and (href.startswith('/') or 'britannica.com' in href):
              if href.startswith('/'): urls.append(href)
              elif 'britannica.com' in href and href not in urls:
                path = href.split('britannica.com')[-1]
                if path.startswith('/'): urls.append(path)
          if urls: break
      for url in urls:
        if url not in unique_urls: unique_urls.append(url)
      self.logger.debug(f"Found {len(unique_urls)} unique URLs")
      return unique_urls
    except Exception as e:
      self.logger.error(f"Error extracting URLs: {e}")
      return []

  def __call__(self, queries:List[str]): self.scrape_queries(queries=queries)

  def _make_request(self, url: str, max_retries: int = 3) -> Optional[requests.Response]:
    for attempt in range(max_retries):
      try:
        time.sleep(random.uniform(self.delay, self.delay + 0.5))
        response = self.session.get(url, timeout=10)

        if response.status_code == 200: return response
        elif response.status_code == 429:
          wait_time = (2 ** attempt) + random.uniform(1, 3)
          self.logger.warning(f"Rate limited. Waiting {wait_time:.1f}s before retry {attempt + 1}")
          time.sleep(wait_time)
        else: self.logger.warning(f"HTTP {response.status_code} for URL: {url}")

      except requests.RequestException as e:
        self.logger.error(f"Request failed (attempt {attempt + 1}): {e}")
        if attempt < max_retries - 1: time.sleep(random.uniform(1, 3))
    return None

  def _extract_article_content(self, url_path: str) -> Optional[str]:
    full_url = urljoin(self.BASE_URL, url_path)
    response = self._make_request(full_url)
    if not response: return None
    try:
      soup = BeautifulSoup(response.content, 'html.parser')
      paragraphs = soup.find_all('p')
      content_parts = []
      for p in paragraphs:
        text = p.get_text(strip=True)
        if text and "Our editors will review what you've submitted" not in text: content_parts.append(text)
      if content_parts:
        content = '\n'.join(content_parts)
        content = re.sub(r'&\w+;', '', content)
        content = re.sub(r'\s+', ' ', content)
        self.total_pages += 1
        return content
    except Exception as e: self.logger.error(f"Error extracting content from {full_url}: {e}")
    return None

  def _process_query(self, query: str) -> List[str]:
    all_urls = []

    for page in range(1, self.max_pages + 1):
      search_url = build_search_url(query, page)
      response = self._make_request(search_url)
      if not response:
        self.logger.warning(f"Failed to fetch search page {page} for query: {query}")
        continue
      urls = self._extract_article_urls(response)
      if not urls:
        self.logger.info(f"No more URLs found at page {page} for query: {query}")
        break
      all_urls.extend(urls)
      self.logger.debug(f"Found {len(urls)} URLs on page {page} for query: {query}")
    self.total_urls += len(all_urls)
    return all_urls

  def _scrape_articles_concurrent(self, urls: List[str]) -> None:
    filepath = os.path.join(self.directory, f"{self.filename}.txt")

    with ThreadPoolExecutor(max_workers=self.max_workers) as executor, \
      open(filepath, 'a', encoding='utf-8') as file:
      future_to_url = {executor.submit(self._extract_article_content, url): url for url in urls}

      for future in as_completed(future_to_url):
        content = future.result()
        if content:
          file.write(f"{content}\n\n")
          file.flush()

  def scrape_queries(self, queries: List[str]) -> None:
    if not queries:
      raise ValueError("Search queries cannot be empty")

    start_time = timeit.default_timer()
    try:
      self.logger.info(f"Starting scraping for {len(queries)} queries")

      for query in tqdm(queries, desc="Processing queries"):
        self.logger.info(f"Processing query: {query}")
        urls = self._process_query(query)
        if urls:
          self.logger.info(f"Scraping {len(urls)} articles for query: {query}")
          self._scrape_articles_concurrent(urls)
        else: self.logger.warning(f"No URLs found for query: {query}")

      self.total_time = timeit.default_timer() - start_time
      if self.metrics: self._display_metrics()

    except Exception as e:
      self.logger.error(f"Error during scraping: {e}")
      raise
    finally: self.session.close()

  def _display_metrics(self) -> None:
    def format_time(seconds): return f"{seconds:.2f}s" if seconds < 60 else f"{seconds/60:.2f}m" if seconds < 3600 else f"{seconds/3600:.2f}h"
    success_rate = (self.total_pages / self.total_urls * 100) if self.total_urls > 0 else 0
    avg_time_per_page = self.total_time / self.total_pages if self.total_pages > 0 else 0
    
    print(f"\n{'='*50}")
    print("BRITANNICA SCRAPING METRICS")
    print(f"{'='*50}")
    print(f"Total URLs discovered: {self.total_urls}")
    print(f"Articles successfully scraped: {self.total_pages}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Total time: {format_time(self.total_time)}")
    print(f"Average time per article: {avg_time_per_page:.2f}s")
    print(f"{'='*50}")

    self.logger.info(f"Scraping completed - URLs: {self.total_urls}, Pages: {self.total_pages}, Time: {self.total_time:.2f}s")