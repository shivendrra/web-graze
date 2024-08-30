from typing import *
from tqdm import tqdm
import json
import os
import logging
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import timeit

logging.basicConfig(filename="youtube_fetch.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def get_captions(videoId):
  try:
    captions = YouTubeTranscriptApi.get_transcript(videoId, languages=["en"], preserve_formatting=True)
    if captions:
      formatted_captions = [caption["text"] for caption in captions]
      transcript = "\n".join(formatted_captions)
      return transcript, True
    else:
      return "", False
  except TranscriptsDisabled as e:
    logging.error(f"Error while fetching the videoId: {videoId} 's transcripts: \n{str(e)}")
    return "", False
  except Exception as e:
    logging.error(f"An exception occured while fetching videoId: {videoId} \n{str(e)}")
    return "", False

class Youtube:
  def __init__(self, api_key:str, filepath:str, max_results:int=50, metrics:bool=False) -> None:
    self.api_key = api_key
    self.directory, filename_with_ext = os.path.split(filepath)
    self.filename, ext = os.path.splitext(filename_with_ext)
    self.filename = self.filename.strip()
    if not os.path.exists(self.directory):
      os.makedirs(self.directory)
    self.youtube_build = build('youtube', 'v3', developerKey=api_key)
    self.maxResults = max_results
    self.metrics = metrics
    self.videoNo = 0
    self.total_time = 0
    self.valid_videoNo = 0
  
  def __call__(self, channel_ids:list[str], videoUrls:bool=False) -> str:
    if channel_ids is not None:
      for channelId in channel_ids:
        assert isinstance(channelId, str) and len(channelId) == 24 and channelId.startswith("UC"), "Invalid YouTube channel ID"
        videoIds = self.fetch_url(channelId)
        if videoUrls:
          urldict = []
          for i in videoIds:
            videoLink = f"https://www.youtube.com/watch?v={i}"
            urldict.append(videoLink)
          self.write_links_in_json(urldict)
        else:
          del videoIds
    if self.metrics:
      self.get_metrics()
    else:
      raise ValueError("Channel_Ids can't be empty")
  
  def fetch_url(self, channelId):
    next_page_token = None
    videoIds = []
    while True:
      response = self.youtube_build.channels().list(
        part='snippet', id=channelId
      ).execute()
      channel_name = response["items"][0]["snippet"]["title"]

      response = self.youtube_build.channels().list(
        part="contentDetails", id=channelId
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
      else:
        logging.error(f"can't find any available video for channel id: {channelId}")
    start_time = timeit.default_timer()
    with tqdm(total=len(videoIds), desc=f"Fetching Captions for channelId: {channel_name}") as pbar:
      for ids in videoIds:
        transcripts, _captions = get_captions(videoId=ids)
        if _captions is True:
          self.write_in_file(transcripts)
          self.valid_videoNo += 1
        self.videoNo += 1
        pbar.update(1)
    end_time = timeit.default_timer()
    self.total_time += end_time - start_time
    return videoIds
  
  def get_metrics(self):
    def format_time(seconds):
      if seconds < 60:
        return f"{seconds:.2f} seconds"
      elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
      else:
        return f"{seconds / 3600:.2f} hours"

    print("\n")
    print("Youtube video caption fetching metrics:\n")
    print("-------------------------------------------")
    print(f"Total videos fetched: {self.videoNo}")
    print(f"Total videos that had captions: {self.valid_videoNo}")
    print(f"Total time taken: {format_time(self.total_time)}")
    print("-------------------------------------------")
  
  def write_in_file(self, transcripts):
    filepath = os.path.join(self.directory, f"{self.filename}.txt")
    with open(f"{filepath}", "a", encoding="utf-8") as outfile:
      outfile.write(transcripts)

  def write_links_in_json(self, urls):
    filepath = os.path.join(self.directory, f"{self.filename}.json")
    with open(f"{filepath}", "a", encoding="utf-8") as outfile:
      json.dump(urls, outfile, indent=2)