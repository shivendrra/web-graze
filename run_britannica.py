""" 
  --> sample script for collecting data from britannica.com
"""

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

from britannica import Scrapper, searchQueries
sq = searchQueries()
queries = sq()

outfile = f"../Datasets/britannica_{len(queries)}.txt"
bs = Scrapper(search_queries=queries, max_limit=10)
bs(out_file=outfile)