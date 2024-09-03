from webgraze import Pexels
from webgraze.queries import Queries

queries = Queries("images")
scraper = Pexels(directory="./images", metrics=True)
scraper(topics=queries())