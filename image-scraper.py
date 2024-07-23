import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

from config import num_images, websites

def scrape_images(num_images, websites):
    """
    Scrape images from the given websites and save them in a folder.

    Args:
        num_images (int): The number of images to be scraped.
        websites (list or str): A list of website URLs or a single website URL.

    Returns:
        None
    """

    # Create a folder to store the images
    folder_name = "scraped_images"
    os.makedirs(folder_name, exist_ok=True)

    # Convert the input to a list if it's a single website URL
    if isinstance(websites, str):
        websites = [websites]

    # Keep track of the number of images scraped
    images_scraped = 0

    for website in websites:
        try:
            # Initialize a queue for DFS
            queue = deque([website])
            visited_urls = set()

            while queue:
                current_url = queue.popleft()
                domain = f"{urlparse(current_url).scheme}://{urlparse(current_url).netloc}"

                # Skip if the URL has already been visited
                if current_url in visited_urls:
                    continue

                visited_urls.add(current_url)
                response = requests.get(current_url)
                response.raise_for_status()  # Raise an exception for non-2xx status codes
                soup = BeautifulSoup(response.content, 'html.parser')

                # Find all image tags on the page
                image_tags = soup.find_all('img')

                for image_tag in image_tags:
                    image_url = urljoin(current_url, image_tag.get('src'))

                    # Check if we've reached the desired number of images
                    if images_scraped >= num_images:
                        return

                    try:
                        # Download the image
                        image_data = requests.get(image_url).content

                        # Save the image
                        image_name = f"image_{images_scraped}.jpg"
                        image_path = os.path.join(folder_name, image_name)
                        with open(image_path, 'wb') as f:
                            f.write(image_data)

                        print(f"Downloaded image: {image_url}")
                        images_scraped += 1

                    except Exception as e:
                        print(f"Error downloading image: {image_url}, {e}")

                # Find all links on the page and add them to the queue
                links = soup.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href.startswith('/'):
                        href = domain + href
                    elif not href.startswith('http'):
                        continue
                    if urlparse(href).netloc == urlparse(current_url).netloc:
                        queue.append(href)

        except Exception as e:
            print(f"Error scraping website: {website}, {e}")

    print(f"Scraped {images_scraped} images and saved them in {folder_name} folder.")

scrape_images(num_images, websites)