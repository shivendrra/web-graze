"""
  --> sample script to collect data from wikipedia.com
"""

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
import timeit

from graze import wikipedia

wiki = wikipedia()

start_time = timeit.default_timer()
wiki(out_file='./output.txt')
end_time = timeit.default_timer()

print(f"total time taken: {((end_time - start_time) / 60):2f} mins")