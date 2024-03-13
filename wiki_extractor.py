# import os
# import timeit
# import requests
# from bs4 import BeautifulSoup as bs
# from tqdm import tqdm
# from concurrent.futures import ThreadPoolExecutor

# class WikiScraper:
#     def __init__(self):
#         self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
#         self.total_urls = 0

#     def scrape_urls(self, urls_batch, out_file):
#         with ThreadPoolExecutor(max_workers=10) as executor:
#             futures = {executor.submit(self.scrapper, url): url for url in urls_batch}
#             for future in tqdm(futures, desc="Scrapping URLs in batch"):
#                 url = futures[future]
#                 out_page = future.result()
#                 if out_page is not None:
#                     with open(out_file, 'a', encoding='utf-8') as outfile:
#                         for paragraph in out_page:
#                             text = paragraph.get_text()
#                             outfile.write(text)
#                 else:
#                     continue

#     def scrape_from_file(self, url_file, out_file, batch_size=100):
#         with open(url_file, 'r', encoding='utf-8') as f:
#             urls = f.readlines()

#         for i in range(0, len(urls), batch_size):
#             urls_batch = urls[i:i+batch_size]
#             self.scrape_urls(urls_batch, out_file)
        
#         print(f'Total fetched URLs: {(self.total_urls/1e5):.2f}k')

#     def scrapper(self, url):
#         r = requests.get(url.strip(), headers=self.headers)
#         if r.status_code == 200:
#             soup = bs(r.content, 'html.parser')
#             paragraphs = soup.find_all('p')
#             self.total_urls += 1
#             return paragraphs
#         else:
#             pass

# if __name__ == "__main__":
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     os.chdir(current_dir)
#     scraper = WikiScraper()
#     url_file = 'extracted_urls.txt'
#     output_file = 'parallel_outputs.txt'

#     start_time = timeit.default_timer()
#     scraper.scrape_from_file(url_file, output_file, batch_size=1000)
#     print(f"Total time taken: {((timeit.default_timer() - start_time)/3600):.2f}hrs")

import os
import timeit
import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class WikiScraper:
    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        self.processed_urls = set()

    def scrape_url(self, url):
        out_page = self.scrapper(url.strip())
        if out_page is not None:
            text = '\n'.join([paragraph.get_text() for paragraph in out_page])
            return text
        else:
            return ''

    def scrape_from_file(self, url_file, out_file, batch_size=100):
        with open(url_file, 'r', encoding='utf-8') as f:
            urls = f.readlines()

        urls = list(set([url.strip() for url in urls]))

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for i in range(0, len(urls), batch_size):
                urls_batch = urls[i:i+batch_size]
                for url in urls_batch:
                    if url not in self.processed_urls:
                        future = executor.submit(self.scrape_url, url)
                        futures.append(future)
                        self.processed_urls.add(url)

            with open(out_file, 'a', encoding='utf-8') as outfile:
                for future in tqdm(futures, desc="Scrapping URLs"):
                    text = future.result()
                    outfile.write(text)

        print(f'Total fetched URLs: {len(self.processed_urls)}')

    def scrapper(self, url):
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            soup = bs(r.content, 'html.parser')
            paragraphs = soup.find_all('p')
            return paragraphs
        else:
            return None

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    scraper = WikiScraper()
    url_file = 'extracted_urls.txt'
    output_file = 'Datasets/parallel_outputs.txt'

    start_time = timeit.default_timer()
    scraper.scrape_from_file(url_file, output_file, batch_size=1000)
    print(f"Total time taken: {timeit.default_timer() - start_time:.2f} seconds")
