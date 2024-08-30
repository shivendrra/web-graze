import os
import logging
import requests
import base64
from bs4 import BeautifulSoup as bs
import re
from tqdm import tqdm
import timeit

logging.basicConfig(filename="image_downloading.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def download_img(src, img_name):
  try:
    image_data = requests.get(src).content
    with open(img_name, 'wb') as img_file:
      img_file.write(image_data)
  except Exception as e:
    logging.error(f"Error while downloading image: {str(e)}")

def download_base64_img(data, img_name):
  try:
    image_data = base64.b64decode(data)
    with open(img_name, 'wb') as img_file:
      img_file.write(image_data)
  except Exception as e:
    logging.error(f"Error while downloading image: {str(e)}")

class Unsplash:
  def __init__(self, directory:str, metrics:bool=False) -> None:
    self.download_dir = directory
    self.headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246" }
    self.imagesNo = 0
    self.total_time = 0
    self.metrics = metrics
  
  def __call__(self, topics):
    if not topics:
      raise ValueError("Enter some topic, can't be empty")
    self.topicNo = len(topics)
    for topic in topics:
      img_data = self.fetch_url(topic)

    if self.metrics:
      self.get_metrics()

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
    print(f"total topics fetched: {self.topicNo}")
    print(f"Total images downloaded: {self.imagesNo}")
    print(f"Total time taken: {format_time(self.total_time)}")
    print("-------------------------------------------")

  def fetch_url(self, topic):
    formatted_query = '-'.join(topic.split(' '))
    url = f"https://unsplash.com/s/photos/{formatted_query}"

    r = requests.get(url, headers=self.headers)
    if r.status_code == 200:
      html_content = r.content
      soup = bs(html_content, 'html.parser')
      img_tags = soup.find_all('img')

      topic_dir = os.path.join(self.download_dir, formatted_query)
      if not os.path.exists(topic_dir):
        os.makedirs(topic_dir)

      start_time = timeit.default_timer()
      with tqdm(total=len(img_tags), desc=f"Downloading images for '{topic}'") as pbar:
        for idx, img in enumerate(img_tags):
          try:
            img_src = img.get('src')
            if not img_src:
              img_src = img.get('data-src')

            if img_src:
              img_name = os.path.join(topic_dir, f'{idx}.jpg')

              if img_src.startswith('data:image'):
                base64_data = re.sub('^data:image/.+;base64,', '', img_src)
                download_base64_img(base64_data, img_name)
              else:
                download_img(img_src, img_name)
            self.imagesNo += 1
            pbar.update(1)
          except Exception as e:
            logging.error(f"Error while fetching images: {str(e)}")
      end_time = timeit.default_timer()
      self.total_time += end_time - start_time
    else:
      logging.error(f"Failed to fetch the URL: {url}. Status code: {r.status_code}")