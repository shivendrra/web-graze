# web-graze

## Introduction
This repository contains a collection of scripts to scrape content from various sources like YouTube, Wikipedia, and Britannica. It includes functionality to download video captions from YouTube, scrape Wikipedia articles, and fetch content from Britannica.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Queries](#1-queries)
  - [YouTube Scraper](#2-youtube-scraper)
  - [Wikipedia Scraper](#3-wikipedia-scraper)
  - [Unsplash Scraper](#4-unsplash-scraper)
  - [Britannica Scraper](#5-britannica-scraper)
  - [Freesound Scraper](#6-freesound-scraper)
  - [Pexels Scraper](#7-pexels-scraper)
- [Configuration](#configuration)
- [Logging](#logging)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shivendrra/web-graze.git
   cd web-scraper-suite
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

For sample examples, use the [run.py](run.py) that contains example for each type of scraper.

### 1. Queries

This library contains some topics, keywords, search queries & channel ids which you can just load & use it with the respective scrapers.

#### Channel Ids

```python
from webgraze.queries import Queries

queries = Queries(category="channel")
```

#### Search Queries

```python
from webgraze.queries import Queries

queries = Queries(category="search")
```

#### Image Topics

```python
from webgraze.queries import Queries

queries = Queries(category="channel")
```

### 2. YouTube Scraper

The YouTube scraper fetches video captions from a list of channels.

#### Configuration
- Add your YouTube API key to a `.env` file:
  ```env
  yt_key=YOUR_API_KEY
  ```

- Create a `channelIds.json` file with the list of channel IDs:
  ```json
  [
    "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "UCJ0-OtVpF0wOKEqT2Z1HEtA"
  ]
  ```

#### Running the Scraper

```python
import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

api_key = os.getenv('yt_key')

from webgraze import Youtube
from webgraze.queries import Queries

queries = Queries(category="channel")

youtube = Youtube(api_key=api_key, filepath='../transcripts', max_results=50)
youtube(channel_ids=queries(), videoUrls=True)
```

### 3. Wikipedia Scraper

The Wikipedia scraper generates target URLs from provided queries, fetches the complete web page, and writes it to a file.

#### Running the Scraper

```python
from webgraze import Wikipedia
from webgraze.queries import Queries

queries = Queries(category="search")
wiki = Wikipedia(filepath='../data.txt', metrics=True)

wiki(queries=queries(), extra_urls=True)
```

### 4. Unsplash Scraper

The Unsplash Image scraper fetches images based on given topics & saves them in their respective folders

#### Configuration
- Define your search queries like this:
  ```python
  search_queries = ["topic1", "topic2", "topic3"]
  ```

#### Running the Scraper

```python
from webgraze import Unsplash
from webgraze.queries import Queries

topics = Queries("images")

image = Unsplash(directory='../images', metrics=True)
image(topics=topics())
```

#### Output:
```shell
Downloading 'american football' images:
Downloading : 100%|██████████████████████████| 176/176 [00:30<00:00,  5.72it/s]

Downloading 'indian festivals' images:
Downloading : 100%|██████████████████████████| 121/121 [00:30<00:00,  7.29it/s]
```

### 5. Britannica Scraper

The Britannica scraper generates target URLs from provided queries, fetches the complete web page, and writes it to a file.

#### Running the scraper

```python
from webgraze import Britannica
from webgraze.queries import Queries

queries = Queries(category="search")
scraper = Britannica(filepath='../data.txt', metrics=True)

scraper(queries=queries())
```

### 6. Freesound Scraper

Scraper to download & save audios from [freesound.org](https://freesound.org/) using its official API. Saves audios in different directories according to the topics.

#### Running the scraper

```python
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("freesound_key")

from webgraze import Freesound

sound = Freesound(api_key=API_KEY, download_dir="audios", metrics=True)
sound(topics=["clicks", "background", "nature"])
```

#### Output

```shell
Downloading 'clicks' audio files:
Response status code: 200
Downloading 'clicks' audio files: 100%|██████████████████████████████| 10/10 [00:20<00:00,  2.01s/it] 

Downloading 'background' audio files:
Response status code: 200
Downloading 'background' audio files: 100%|██████████████████████████████| 10/10 [00:53<00:00,  5.37s/it] 

Downloading 'nature' audio files:
Response status code: 200
Downloading 'nature' audio files: 100%|██████████████████████████████| 10/10 [01:57<00:00, 11.78s/it] 

Freesound Scraper Metrics:

-------------------------------------------
Total topics fetched: 3
Total audio files downloaded: 30
Total time taken: 3.26 minutes
-------------------------------------------
```

### 7. Pexels Scraper

Scrapes & downloads pictures from [pexels.com](https://www.pexels.com/) & saves them in individual directory topic-wise.

#### Running the scraper

```python
from webgraze import Pexels
from webgraze.queries import Queries

queries = Queries("images")
scraper = Pexels(directory="./images", metrics=True)
scraper(topics=queries())
```

#### Output
```shell
Downloading 'american football' images:
Downloading: 100%|████████████████████████████████| 24/24 [00:03<00:00,  7.73it/s]

Downloading 'india' images:
Downloading: 100%|████████████████████████████████| 27/27 [00:04<00:00,  5.99it/s]

Downloading 'europe' images:
Downloading: 100%|████████████████████████████████| 24/24 [00:06<00:00,  3.55it/s]
```

## Configuration

- **API Keys and other secrets:** Ensure that your API keys and other sensitive data are stored securely and not hard-coded into your scripts.

- **Search Queries:** The search queries for Wikipedia and Britannica scrapers are defined in `queries.py`.

## Logging

Each scraper logs errors to respective `.log` file. Make sure to check this file for detailed error messages & troubleshooting information.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

Check out [CONTRIBUTING.md](https://github.com/shivendrra/web-graze/blob/main/CONTRIBUTING.md) for more details

## License

This project is licensed under the MIT License.