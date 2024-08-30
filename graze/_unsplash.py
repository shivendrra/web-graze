import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

import logging
logging.basicConfig(filename='image_downloading.log', level=logging.ERROR)

import requests
from bs4 import BeautifulSoup as bs
import base64
import re
import json
from tqdm import tqdm

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

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

def fetch_url(topic):
  formatted_query = '-'.join(topic.split(' '))
  url = f"https://unsplash.com/s/photos/{formatted_query}"

  r = requests.get(url, headers=headers)
  if r.status_code == 200:
    html_content = r.content
    soup = bs(html_content, 'html.parser')
    img_tags = soup.find_all('img')

    topic_dir = f'../images/{formatted_query}'
    if not os.path.exists(topic_dir):
      os.makedirs(topic_dir)

    with tqdm(total=len(img_tags), desc=f"Downloading ") as pbar:
      for idx, img in enumerate(img_tags):
        try:
          img_src = img.get('src')
          if not img_src:
            img_src = img.get('data-src')

          if img_src:
            img_name = f'{topic_dir}/{idx}.jpg'

            if img_src.startswith('data:image'):
              base64_data = re.sub('^data:image/.+;base64,', '', img_src)
              download_base64_img(base64_data, img_name)
            else:
              download_img(img_src, img_name)
          pbar.update(1)
        except Exception as e:
          logging.error(f"Error while fetching images: {str(e)}")
  else:
    logging.error(f"Failed to fetch the URL: {url}. Status code: {r.status_code}")

def unsplash(topics=None):
  if topics:
    target_topics = topics
  else:
    with open('./imageQuery.json', 'r') as infile:
      target_topics = json.load(infile)
  
  for topic in target_topics:
    print(f"\nDownloading '{topic}' images:")
    fetch_url(topic)