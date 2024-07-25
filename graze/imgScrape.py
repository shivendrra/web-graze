import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def create_directory(topic):
  directory = f'images/{topic}'
  if not os.path.exists(directory):
    os.makedirs(directory)
  return directory

def download_image(url, folder):
  try:
    image_data = requests.get(url).content
    image_name = os.path.join(folder, url.split('/')[-1])
    with open(image_name, 'wb') as image_file:
      image_file.write(image_data)
  except Exception as e:
    print(f"Failed to download {url}. Reason: {e}")

def scrape_images_for_topic(topic):
  print(f"Scraping images for topic: {topic}")
  topic_folder = create_directory(topic)
    
  query = quote(topic)
  url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  image_tags = soup.find_all("img")
  print(image_tags)

  # for img_tag in image_tags:
  #   try:
  #     img_url = img_tag['src']
  #     if not img_url:
  #       img_url = img_tag['data-src']
  #     if img_url:
  #       download_image(img_url, topic_folder)
  #   except Exception as e:
  #     print(f"Failed to process an image tag. Reason: {e}")

topics = [
  "antarctica", "colonization", "world war", "asia", "africa", 
  "australia", "holocaust", "voyages", "biological viruses"
]

for topic in topics:
  scrape_images_for_topic(topic)