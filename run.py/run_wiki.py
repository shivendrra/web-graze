from webgraze import Wikipedia
from webgraze.queries import Queries

queries = Queries(category="search")
wiki = Wikipedia(filepath='../data.txt', metrics=True)

wiki(queries=queries(), extra_urls=True)