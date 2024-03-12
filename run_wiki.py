"""
  --> sample script to collect data from wikipedia.com
"""

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
import timeit
from wikipedia import WikiQueries, WikiScraper
queries = WikiQueries()
scrape = WikiScraper()

start_time = timeit.default_timer()
queries = queries()
output_file = f'../Datasets/wiki_{len(queries)}.txt'
scrape(out_file=output_file, search_queries=queries, extra_urls=True)

print(f"total time taken: {((timeit.default_timer() - start_time)/3660):.2f}hrs")