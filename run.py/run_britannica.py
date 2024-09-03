import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

from webgraze import Britannica
from webgraze.queries import Queries

queries = Queries(category="search")
wiki = Britannica(filepath='../data.txt', metrics=True)

wiki(queries=queries())