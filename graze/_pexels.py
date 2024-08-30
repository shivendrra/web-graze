import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
import requests
import logging
import timeit

logging.basicConfig(filename="pexels_downloading.log", level=logging.ERROR)
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def download_img(url, img_name):
  try:
    image_data = requests.get(url).content
    with open(img_name, 'wb') as img_file:
      img_file.write(image_data)
  except Exception as e:
    logging.error(f"Error downloading image: {e}")

def download_base64_img(data, img_name):
  try:
    image_data = base64.b64decode(data)
    with open(img_name, 'wb') as img_file:
      img_file.write(image_data)
  except Exception as e:
    logging.error(f"Error downloading image: {e}")

class Pexels:
  def __init__(self, directory:str, metrics:bool=False) -> None:
    self.download_dir = directory
    self.imagesNo = 0
    self.total_time = 0
    self.metrics = metrics
    os.makedirs(directory, exist_ok=True)
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  
  def __call__(self, topics:list[str]):
    if not topics:
      raise ValueError("Enter some topic, can't be empty")
    self.topicNo = len(topics)
    for topic in topics:
      print(f"\nDownloading '{topic}' images:")
      self.fetch_images(topic)
    if self.metrics:
      self.get_metrics()
    self.quit()

  def fetch_images(self, query):
    search_url = f"https://www.pexels.com/search/{query}/"
    self.driver.get(search_url)
    time.sleep(3)
    
    img_elements = self.driver.find_elements(By.CSS_SELECTOR, "img[srcset]")
    
    query_dir = os.path.join(self.download_dir, query)
    os.makedirs(query_dir, exist_ok=True)
    
    start_time = timeit.default_timer()
    with tqdm(total=len(img_elements), desc=f"Downloading: ") as pbar:
      for idx, img_element in enumerate(img_elements):
        try:
          img_src = img_element.get_attribute("src")
          img_name = os.path.join(query_dir, f"image_{idx}.jpg")
          if img_src.startswith("data:image"):
            img_data = img_src.split(",")[1]
            download_base64_img(img_data, img_name)
          else:
            download_img(img_src, img_name)
          self.imagesNo += 1
          pbar.update(1)
        except Exception as e:
          logging.error(f"Error processing image: {e}")
    
    end_time = timeit.default_timer()
    self.total_time += end_time - start_time
  
  def get_metrics(self):
    def format_time(seconds):
      if seconds < 60:
        return f"{seconds:.2f} seconds"
      elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
      else:
        return f"{seconds / 3600:.2f} hours"

    print("\nPexels image downloading metrics:\n")
    print("-------------------------------------------")
    print(f"Total topics fetched: {self.topicNo}")
    print(f"Total images downloaded: {self.imagesNo}")
    print(f"Total time taken: {format_time(self.total_time)}")
    print("-------------------------------------------")

  def quit(self):
    self.driver.quit()