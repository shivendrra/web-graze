from webgraze import Youtube
from webgraze.queries import Queries

queries = Queries(category="search")
print(queries())

youtube = Youtube(api_key="AIzaSyBhbYzOh_B3snsiBlCEwI4DdUZbKJVHass", filepath='../transcripts', max_results=50)
youtube(channel_ids=["UC415bOPUcGSamy543abLmRA"], videoUrls=True)