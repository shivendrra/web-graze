# WebGraze Documentation

## Overview

This is a comprehensive web scraping framework designed to collect data from multiple sources including text content, images, audio files, and video transcripts. The framework provides modular scrapers for different platforms with built-in error handling, rate limiting, and performance metrics.

## Architecture

The framework consists of 7 main components:

1. **Britannica Scraper** (`_britannica.py`) - Educational content scraping
2. **Wikipedia Scraper** (`_wiki.py`) - Encyclopedia content extraction
3. **YouTube Transcripts** (`_transcripts.py`) - Video caption fetching
4. **Freesound Audio** (`_freesound.py`) - Audio file downloading
5. **Unsplash Images** (`_unsplash.py`) - Image collection
6. **Pexels Images** (`_pexels.py`) - Stock photo downloading
7. **Query Manager** (`queries.py`) - Centralized topic management

## Installation & Dependencies

### WebGraze library

```bash
pip install webgraze
```

### Required Python Packages
```bash
pip install requests beautifulsoup4 tqdm selenium webdriver-manager
pip install google-api-python-client youtube-transcript-api
```

### Additional Requirements
- Chrome WebDriver (automatically managed by webdriver-manager)
- API Keys:
  - YouTube Data API v3 key
  - Freesound API key

## Configuration

### topics.json Structure
Create a `topics.json` file with the following structure:

```json
{
  "search_topics": ["artificial intelligence", "machine learning", "data science"],
  "channel_ids": ["UC_channel_id_1", "UC_channel_id_2"],
  "image_topics": ["technology", "nature", "abstract art"]
}
```

## Component Documentation

### 1. Britannica Scraper (`_britannica.py`)

Scrapes educational content from Britannica Encyclopedia with concurrent processing and intelligent rate limiting.

#### Features
- Multi-page search result processing
- Concurrent article scraping with thread pool
- Intelligent rate limiting and retry logic
- Multiple URL extraction strategies
- Comprehensive logging and metrics

#### Usage
```python
from graze._britannica import Britannica

scraper = Britannica(
    filepath="./data/britannica_content.txt",
    max_pages=10,
    metrics=True,
    max_workers=3,
    delay=1.0
)

queries = ["quantum physics", "machine learning", "climate change"]
scraper(queries)
```

#### Parameters
- `filepath` (str): Output file path
- `max_pages` (int): Maximum search pages per query (default: 10)
- `metrics` (bool): Display performance metrics (default: False)
- `max_workers` (int): Concurrent thread count (default: 3)
- `delay` (float): Base delay between requests (default: 1.0)

#### Key Methods
- `scrape_queries(queries)`: Main scraping method
- `_process_query(query)`: Extract URLs from search pages
- `_extract_article_content(url_path)`: Scrape individual articles
- `_make_request(url)`: HTTP request with retry logic

### 2. Wikipedia Scraper (`_wiki.py`)

Extracts content from Wikipedia articles with optional link following for comprehensive coverage.

#### Features
- Primary article content extraction
- Optional related link following
- Robust error handling
- Performance metrics tracking

#### Usage
```python
from graze._wiki import Wikipedia

scraper = Wikipedia(
    filepath="./data/wikipedia_content.txt",
    metrics=True
)

queries = ["artificial intelligence", "quantum computing"]
scraper(queries, extra_urls=True)
```

#### Parameters
- `filepath` (str): Output file path
- `metrics` (bool): Display performance metrics

#### Methods
- `__call__(queries, extra_urls=False)`: Main scraping method
- `extra_urls` (bool): Follow related Wikipedia links

### 3. YouTube Transcripts (`_transcripts.py`)

Fetches video transcripts from YouTube channels using the YouTube Data API.

#### Features
- Channel-based video discovery
- Automatic transcript extraction
- Multi-language support (defaults to English)
- Optional video URL export
- Comprehensive error logging

#### Usage
```python
from graze._transcripts import Youtube

scraper = Youtube(
    api_key="your_youtube_api_key",
    filepath="./data/youtube_transcripts.txt",
    max_results=50,
    metrics=True
)

channel_ids = ["UC_channel_id_1", "UC_channel_id_2"]
scraper(channel_ids, videoUrls=False)
```

#### Parameters
- `api_key` (str): YouTube Data API v3 key
- `filepath` (str): Output file path
- `max_results` (int): Videos per channel (default: 50)
- `metrics` (bool): Display performance metrics
- `videoUrls` (bool): Export video URLs to JSON

### 4. Freesound Audio (`_freesound.py`)

Downloads audio files from Freesound.org using their API.

#### Features
- High-quality MP3 preview downloads
- Organized folder structure by topic
- API-based search and download
- Download progress tracking

#### Usage
```python
from graze._freesound import Freesound

scraper = Freesound(
    api_key="your_freesound_api_key",
    download_dir="./audio_files",
    max_results=10,
    metrics=True
)

topics = ["nature sounds", "electronic music", "ambient"]
scraper(topics)
```

#### Parameters
- `api_key` (str): Freesound API key
- `download_dir` (str): Audio files directory
- `max_results` (int): Files per topic (default: 10)
- `metrics` (bool): Display performance metrics

### 5. Unsplash Images (`_unsplash.py`)

Scrapes images from Unsplash using web scraping techniques.

#### Features
- High-resolution image downloads
- Base64 image handling
- Topic-based organization
- Progress tracking with tqdm

#### Usage
```python
from graze._unsplash import Unsplash

scraper = Unsplash(directory="./unsplash_images", metrics=True)

topics = ["landscape", "technology", "abstract"]
scraper(topics)
```

#### Parameters
- `directory` (str): Image download directory
- `metrics` (bool): Display performance metrics

### 6. Pexels Images (`_pexels.py`)

Downloads stock photos from Pexels using Selenium WebDriver.

#### Features
- Selenium-based dynamic content handling
- Automatic WebDriver management
- Base64 and URL image downloads
- Topic-based folder organization

#### Usage
```python
from graze._pexels import Pexels

scraper = Pexels( directory="./pexels_images", metrics=True)

topics = ["business", "nature", "technology"]
scraper(topics)
```

#### Parameters
- `directory` (str): Image download directory
- `metrics` (bool): Display performance metrics

### 7. Query Manager (`queries.py`)

Centralized management of search topics and channel IDs from JSON configuration.

#### Usage
```python
from graze.queries import Queries

# Get search topics for text scrapers
search_queries = Queries("search")()

# Get channel IDs for YouTube scraper
channel_ids = Queries("channel")()

# Get image topics for image scrapers
image_topics = Queries("images")()
```

#### Categories
- `"search"`: Topics for Britannica and Wikipedia
- `"channel"`: YouTube channel IDs
- `"images"`: Topics for Unsplash and Pexels

## Complete Usage Example

```python
from graze import *

# Initialize scrapers
britannica = Britannica("./data/britannica.txt", metrics=True)
wiki = Wikipedia("./data/wikipedia.txt", metrics=True)
youtube = Youtube("YOUR_API_KEY", "./data/transcripts.txt", metrics=True)
freesound = Freesound("YOUR_API_KEY", "./audio", metrics=True)
unsplash = Unsplash("./images/unsplash", metrics=True)
pexels = Pexels("./images/pexels", metrics=True)

# Load queries
search_topics = Queries("search")()
channel_ids = Queries("channel")()
image_topics = Queries("images")()

# Execute scraping
britannica(search_topics)
wiki(search_topics)
youtube(channel_ids)
freesound(["ambient", "nature"])
unsplash(image_topics)
pexels(image_topics)
```

## Best Practices

### Rate Limiting
- Britannica: Built-in exponential backoff for 429 errors
- Wikipedia: Standard delays between requests
- YouTube: API rate limits handled automatically
- Image scrapers: Selenium implicit waits

### Error Handling
- All scrapers log errors to dedicated log files
- Graceful failure handling with continued processing
- Network timeout protection
- Invalid URL/ID validation

### Performance Optimization
- Concurrent processing where applicable (Britannica)
- Session reuse for HTTP connections
- Progress tracking with tqdm
- Comprehensive metrics collection


## API Requirements

### YouTube Data API v3
1. Enable YouTube Data API v3 in Google Cloud Console
2. Create credentials and get API key
3. Set daily quota limits appropriately

### Freesound API
1. Register at freesound.org
2. Create application to get API key
3. Review rate limits and terms of service

## Troubleshooting

### Common Issues
1. **ChromeDriver Issues**: Automatically resolved by webdriver-manager
2. **API Rate Limits**: Built-in retry logic handles most cases
3. **Network Timeouts**: Configurable timeout settings
4. **Invalid Channel IDs**: Must be 24 characters starting with "UC"

### Log Files
Each scraper maintains detailed logs:
- `britannica_scraper.log`
- `wiki_scraper.log`
- `youtube_fetch.log`
- `freesound_scraper.log`
- `pexels_downloading.log`
- `image_downloading.log`

## Performance Metrics

All scrapers provide detailed metrics including:
- Total items processed
- Success rates
- Processing time
- Average time per item
- Error counts

## Legal Considerations

- Respect robots.txt files
- Follow platform terms of service
- Implement appropriate delays
- Don't overwhelm servers
- Consider copyright implications
- Use downloaded content responsibly

## Future Enhancements

Potential improvements:
- Database storage integration
- REST API wrapper
- Docker containerization
- Enhanced error recovery
- Real-time monitoring dashboard
- Additional platform support