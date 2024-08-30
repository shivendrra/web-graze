import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

api_key = os.getenv('yt_key')

from graze import Youtube
from graze.queries import Queries

queries = Queries(category="channel")

youtube = Youtube(api_key=api_key, filepath='../transcripts', max_results=50)
youtube(channel_ids=queries(), videoUrls=True)