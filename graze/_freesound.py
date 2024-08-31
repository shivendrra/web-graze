import os
import logging
import requests
from tqdm import tqdm
import timeit

logging.basicConfig(filename="freesound_scraper.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

def download_audio_file(url, file_path):
  try:
    response = requests.get(url)
    with open(file_path, 'wb') as audio_file:
      audio_file.write(response.content)
  except Exception as e:
    logging.error(f"Error downloading audio: {str(e)}")

class Freesound:
  def __init__(self, api_key:str, download_dir:str, max_results:int=10, metrics:bool=False) -> None:
    self.api_key = api_key
    self.base_url = "https://freesound.org/apiv2/search/text/"
    self.download_dir = download_dir
    if not os.path.exists(self.download_dir):
      os.makedirs(self.download_dir)
    self.max_results = max_results
    self.metrics = metrics
    self.total_files = 0
    self.total_time = 0

  def __call__(self, topics:list[str]):
    if not topics:
      raise ValueError("Topics can't be empty.")
    
    self.total_topics = len(topics)
    self.total_time = timeit.default_timer()
    for topic in topics:
      print(f"\nDownloading '{topic}' audio files:")
      self.fetch_audio_files(topic)
    self.total_time = timeit.default_timer() - self.total_time
    
    if self.metrics:
      self.get_metrics()

  def fetch_audio_files(self, query:str):
    params = {
      'query': query,
      'token': self.api_key,
      'page_size': self.max_results,
      'fields': 'id,previews,original_filename'
    }
    response = requests.get(self.base_url, params=params)
    if response.status_code == 200:
      data = response.json()
      audio_files = data['results']
      if not audio_files:
        print(f"No audio files found for the topic '{query}'")
        return
      
      query_dir = os.path.join(self.download_dir, query.replace(' ', '_'))
      if not os.path.exists(query_dir):
        os.makedirs(query_dir)
      
      for audio in tqdm(audio_files, desc=f"Downloading '{query}' audio files"):
        audio_url = audio['previews']['preview-hq-mp3']
        audio_filename = os.path.join(query_dir, f"{audio['id']}_{audio['original_filename']}.mp3")
        download_audio_file(audio_url, audio_filename)
        self.total_files += 1
    else:
      logging.error(f"Failed to fetch data for '{query}'. Status code: {response.status_code}")
    
  def get_metrics(self):
    print("\nFreesound Scraper Metrics:\n")
    print("-------------------------------------------")
    print(f"Total topics fetched: {self.total_topics}")
    print(f"Total audio files downloaded: {self.total_files}")
    if self.total_time < 60:
      print(f"Total time taken: {self.total_time:.2f} seconds")
    elif self.total_time < 3600:
      print(f"Total time taken: {self.total_time/60:.2f} minutes")
    else:
      print(f"Total time taken: {self.total_time/3600:.2f} hours")
    print("-------------------------------------------")