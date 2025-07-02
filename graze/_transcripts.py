from typing import List, Tuple, Optional
from tqdm import tqdm
import json, os, logging, timeit
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from concurrent.futures import ThreadPoolExecutor, as_completed

class YouTubeTranscriptFetcher:
  def __init__(self, api_key: str, filepath: str, max_results: int = 50, metrics: bool = False, max_workers: int = 5):
    self.api_key, self.max_results, self.metrics, self.max_workers = api_key, max_results, metrics, max_workers
    self.directory, filename_with_ext = os.path.split(filepath)
    self.filename = os.path.splitext(filename_with_ext)[0].strip()
    self.video_count, self.valid_video_count, self.total_time = 0, 0, 0
    os.makedirs(self.directory, exist_ok=True)

    self.logger = logging.getLogger(__name__)
    handler = logging.FileHandler("youtube_fetch.log")
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    self.logger.addHandler(handler)
    self.logger.setLevel(logging.INFO)
    
    try:
      self.youtube = build('youtube', 'v3', developerKey=api_key)
      self.logger.info("YouTube API client initialized successfully")
    except Exception as e:
      self.logger.error(f"Failed to initialize YouTube API: {e}")
      raise

  def _get_transcript(self, video_id: str) -> Tuple[str, bool]:
    try:
      captions = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"], preserve_formatting=True)
      transcript = "\n".join([caption["text"] for caption in captions]) if captions else ""
      return transcript, bool(transcript)
    except TranscriptsDisabled:
      self.logger.warning(f"Transcripts disabled for video: {video_id}")
      return "", False
    except Exception as e:
      self.logger.error(f"Error fetching transcript for {video_id}: {e}")
      return "", False

  def _fetch_video_ids(self, channel_id: str) -> Tuple[List[str], str]:
    try:
      channel_response = self.youtube.channels().list(part='snippet,contentDetails', id=channel_id).execute()
      
      if not channel_response.get("items"):
        self.logger.error(f"No channel found for ID: {channel_id}")
        return [], ""

      channel_info = channel_response["items"][0]
      channel_name = channel_info["snippet"]["title"]
      playlist_id = channel_info["contentDetails"]["relatedPlaylists"]["uploads"]
      
      video_ids, next_page_token = [], None
      
      while True:
        playlist_response = self.youtube.playlistItems().list(part="contentDetails", playlistId=playlist_id, maxResults=self.max_results, pageToken=next_page_token).execute()
        video_ids.extend([item["contentDetails"]["videoId"] for item in playlist_response.get("items", [])])
        next_page_token = playlist_response.get('nextPageToken')        
        if not next_page_token: break

      self.logger.info(f"Fetched {len(video_ids)} video IDs for channel: {channel_name}")
      return video_ids, channel_name
      
    except Exception as e:
      self.logger.error(f"Error fetching video IDs for channel {channel_id}: {e}")
      return [], ""

  def _process_videos_concurrent(self, video_ids: List[str], channel_name: str) -> None:
    filepath = os.path.join(self.directory, f"{self.filename}.txt")

    with ThreadPoolExecutor(max_workers=self.max_workers) as executor, \
      tqdm(total=len(video_ids), desc=f"Processing {channel_name}") as pbar:
      future_to_video = {executor.submit(self._get_transcript, vid): vid for vid in video_ids}

      with open(filepath, "a", encoding="utf-8") as file:
        for future in as_completed(future_to_video):
          transcript, success = future.result()
          if success:
            file.write(f"{transcript}\n\n")
            self.valid_video_count += 1
          self.video_count += 1
          pbar.update(1)

  def _save_video_urls(self, video_ids: List[str]) -> None:
    urls = [f"https://www.youtube.com/watch?v={vid}" for vid in video_ids]
    filepath = os.path.join(self.directory, f"{self.filename}.json")

    with open(filepath, "w", encoding="utf-8") as file:
      json.dump(urls, file, indent=2)
    self.logger.info(f"Saved {len(urls)} video URLs to {filepath}")

  def process_channels(self, channel_ids: List[str], save_urls: bool = False) -> None:
    if not channel_ids: raise ValueError("Channel IDs cannot be empty")

    for channel_id in channel_ids:
      if not (isinstance(channel_id, str) and len(channel_id) == 24 and channel_id.startswith("UC")): raise ValueError(f"Invalid YouTube channel ID: {channel_id}")    
    start_time = timeit.default_timer()
    try:
      for channel_id in channel_ids:
        self.logger.info(f"Processing channel: {channel_id}")
        video_ids, channel_name = self._fetch_video_ids(channel_id)
        
        if not video_ids: continue
        if save_urls: self._save_video_urls(video_ids)
        else: self._process_videos_concurrent(video_ids, channel_name)
      self.total_time = timeit.default_timer() - start_time
      if self.metrics: self._display_metrics()

    except Exception as e:
      self.logger.error(f"Error processing channels: {e}")
      raise

  def _display_metrics(self) -> None:
    def format_time(seconds): return f"{seconds:.2f}s" if seconds < 60 else f"{seconds/60:.2f}m" if seconds < 3600 else f"{seconds/3600:.2f}h"
    success_rate = (self.valid_video_count / self.video_count * 100) if self.video_count > 0 else 0

    print(f"\n{'='*50}")
    print("YOUTUBE TRANSCRIPT FETCHING METRICS")
    print(f"{'='*50}")
    print(f"Total videos processed: {self.video_count}")
    print(f"Videos with captions: {self.valid_video_count}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Total time: {format_time(self.total_time)}")
    print(f"{'='*50}")

    self.logger.info(f"Metrics - Total: {self.video_count}, Valid: {self.valid_video_count}, Time: {self.total_time:.2f}s")