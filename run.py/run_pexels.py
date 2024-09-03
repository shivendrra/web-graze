from graze import Pexels
from graze.queries import Queries

queries = Queries("images")
scraper = Pexels(directory="./images", metrics=True)
scraper(topics=queries())