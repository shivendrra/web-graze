"""
  --> sample script to collect transcripts from youtube videos
"""

import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

api_key = os.getenv('yt_key')

from graze import youtube

scraper = youtube(api_key=api_key, filepath='./output.txt')
scraper()