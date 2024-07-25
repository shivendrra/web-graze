from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import logging
from tqdm import tqdm
import json
import os

logging.basicConfig(filename='youtube_fetch.log', level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

class Youtube:
  def __init__(self, api_key, filepath) -> None:
    self.api_key = api_key
    self.filepath = filepath
    self.youtube = build('youtube', 'v3', developerKey=api_key)
  
  def __call__(self, channel_id=None):
    if channel_id:
      self.channelData = [channel_id]
    else:
      with open('./channelIds.json', 'r') as infile:
        self.channelData = json.load(infile)
    self.run()

  def fetch_url(self, channelId):
    next_page_token = None
    videoIds = []
    while True:
      response = self.youtube.channels().list(
        part='contentDetails', id=channelId
      ).execute()

      if 'items' in response and response['items']:
        playlistId = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        playlistsRes = self.youtube.playlistItems().list(
          part='contentDetails', playlistId=playlistId,
          maxResults=100, pageToken=next_page_token
        ).execute()

        videoIds.extend([item['contentDetails']['videoId'] for item in playlistsRes.get('items', [])])
        next_page_token = playlistsRes.get('nextPageToken')
        if not next_page_token:
          break
    return videoIds
  
  def convert(self, result):
    with open(f"{self.filepath}.json", 'w') as outfile:
      json.dump(result, outfile, indent=2)
      print("Data written successfully in JSON file")
  
  def get_captions(self, videoId):
    try:
      raw_transcripts = []
      videoNo = 0
      for ids in videoId:
        try:
          captions = YouTubeTranscriptApi.get_transcript(
            ids, languages=['en'], preserve_formatting=True
          )
          if captions:
            formatted_captions = [{'text': caption['text']} for caption in captions]
            raw_transcripts.append(formatted_captions)
            videoNo += 1
          else:
            continue
        except TranscriptsDisabled as e:
          logging.error(f"Error while fetching the videos: {str(e)}")
        except Exception as e:
          logging.error(f"Error while fetching the videos: {str(e)}")
      print(f"Number of videos that had captions: {videoNo}")
      return raw_transcripts
    except Exception as e:
      logging.error(f"Error while fetching the videos: {str(e)}")
  
  def save_captions(self, transcripts):
    with open(f"{self.filepath}.txt", 'a', encoding='utf-8') as file:
      for video_captions in transcripts:
        for line in video_captions:
          file.write(line['text'])
  
  def run(self):
    urldict = []
    for channel_id in tqdm(self.channelData, desc="Fetching captions from Youtube: "):
      video_ids = self.fetch_url(channel_id)
      captions = self.get_captions(video_ids)
      self.save_captions(captions)
      for i in video_ids:
        videoLink = f"https://www.youtube.com/watch?v={i}"
        urldict.append(videoLink)
    
    self.convert(urldict)