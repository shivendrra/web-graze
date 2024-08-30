from typing import *
from pathlib import Path
from tqdm import tqdm
import json
import os
import logging
from googleapiclient.discovery import build

logging.basicConfig(filename="youtube_fetch.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def get_captions(languages):
  pass

class Youtube:
  def __init__(self, api_key:str, filepath:Union[str, Path], max_results:int=50, languages:list[str]=None, metrics:bool=False) -> None:
    self.api_key = api_key
    self.filepath = filepath
    self.youtube_build = build('youtube', 'v3', developerKey=api_key)
    self.maxResults = max_results
    self.languages = languages
    self.metrics = metrics
  
  def fetch_url(self, channelIds):
    next_page_token = None
    videoIds = []
    while True:
      response = self.youtube_build.channels().list(
        part="contentDetails", id=channelIds
      ).execute()

      if "items" in response and response["items"]:
        playlistId = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        playlistRes = self.youtube_build.playlistItems().list(
          part="contentDetails", playlistId=playlistId,
          maxResults=self.maxResults, pageToken=next_page_token
        ).execute()

        for item in playlistRes.get("items", []):
          videoIds.extend([item["contentDetails"]["videoId"]])
        next_page_token = playlistRes.get('nextPageToken')
        if not next_page_token:
          break
    return videoIds
  
  def get_metrics(self):
    pass

  def write_in_file(self, transcripts):
    pass

  def write_links_in_json(self, urls):
    with open(f"{self.filepath}.json", 'w') as outfile:
      json.dump(urls, outfile, indent=2)
      print(f"Data written successfully in JSON at the filepath={self.filepath}.json")