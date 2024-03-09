import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

import json
from googleapiclient.discovery import build
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi
import logging
import timeit
from tqdm import tqdm

class TranscriptsCollector:
  def __init__(self, api_key=None) -> None:
    self.api_key = api_key
    self.youtube = build('youtube', 'v3', developerKey=self.api_key)
    self.videoNo = 0
    self.ignoredVids = 0

  def get_video_ids(self, ids):
    next_page_token = None
    videoIds = []

    while True:
      channel_res = self.youtube.channels().list(
        part='contentDetails,snippet', id=ids
      ).execute()
      if 'items' in channel_res and channel_res['items']:
        channel_name = channel_res["items"][0]["snippet"]["title"]
        playlistId = channel_res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        playlistResult = self.youtube.playlistItems().list(
          part='contentDetails', playlistId=playlistId,
          maxResults=100, pageToken=next_page_token
        ).execute()

        videoIds.extend([item['contentDetails']['videoId'] for item in playlistResult.get('items', [])])
        next_page_token = playlistResult.get('nextPageToken')
        if not next_page_token:
          break

    return videoIds

  def build_urls(self):
    pass

  def __call__(self, channel_ids, max_results=100, max_video_limit=None, videoLinks=False):
    for ids in channel_ids:
      videoIds = self.get_video_ids(ids)

  def generate_summary(self):
    pass