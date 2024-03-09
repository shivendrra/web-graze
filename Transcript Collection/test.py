import json
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
print(f"current directory: {current_directory}")

query_file = '../britannica/search_queries.json'
out_file = 'britannica_ouptut.txt'
out_path = os.path.join(current_directory, '../data', out_file)
max_limit = 10

with open(query_file, 'r') as file:
  search_queries = json.load(file)
print(search_queries)

from britannica import Scrapper

bs = Scrapper(search_queries, max_limit)
bs(out_file)