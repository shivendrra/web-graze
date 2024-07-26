# web-graze

## Introduction
This repository contains a collection of scripts to scrape content from various sources like YouTube, Wikipedia, and Britannica. It includes functionality to download video captions from YouTube, scrape Wikipedia articles, and fetch content from Britannica.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [YouTube Scraper](#youtube-scraper)
  - [Wikipedia Scraper](#wikipedia-scraper)
  - [Britannica Scraper](#britannica-scraper)
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

### YouTube Scraper

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
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('yt_key')

from graze import youtube

scraper = youtube(api_key=api_key, filepath='./output.txt')
scraper()
```

### Wikipedia Scraper

The Wikipedia scraper generates target URLs from provided queries, fetches the complete web page, and writes it to a file.

#### Configuration
- Define your search queries in `queries.py`:
  ```python
  class WikiQueries:
      def __init__(self):
          self.search_queries = ["topic1", "topic2", "topic3"]
      
      def __call__(self):
          return self.search_queries
  ```

#### Running the Scraper

```python
from graze import wikipedia

wiki = wikipedia()
wiki(out_file='./output.txt')
```

### Britannica Scraper

The Britannica scraper fetches content based on search queries and writes it to a file.

#### Configuration
- Define your search queries in `queries.py`:
  ```python
  class BritannicaQueries:
      def __init__(self):
          self.search_queries = ["topic1", "topic2", "topic3"]
      
      def __call__(self):
          return self.search_queries
  ```

#### Running the Scraper

```python
from graze import britannica

scraper = britannica(max_limit=20)
scraper(out_file='./output.txt')
```

### Unsplash Scraper

The Unsplash Image scraper fetches images based on given topics & saves them in their respective folders

#### Configuration
- Define your search queries in `queries.py`:
  ```python
  search_queries = ["topic1", "topic2", "topic3"]
  ```

#### Running the Scraper

```python
import graze

scraper = graze.unsplash(topics=search_queries)
```

#### Output:
```shell

Downloading 'american football' images:
Downloading : 100%|██████████████████████████| 176/176 [00:30<00:00,  5.72it/s]

Downloading 'indian festivals' images:
Downloading : 100%|██████████████████████████| 121/121 [00:30<00:00,  7.29it/s]
```

## Configuration

- **API Keys and other secrets:** Ensure that your API keys and other sensitive data are stored securely and not hard-coded into your scripts.

- **Search Queries:** The search queries for Wikipedia and Britannica scrapers are defined in `queries.py`.

## Logging

The YouTube scraper logs errors to `youtube_fetch.log`. Make sure to check this file for detailed error messages and troubleshooting information.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

Check out [CONTRIBUTING.md](https://github.com/shivendrra/web-graze/blob/main/CONTRIBUTING.md) for more details

## License

This project is licensed under the MIT License.