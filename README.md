# web-graze

## Introduction
this repo contains codes that would help you to scrape data from various sites on the internet like wikipedia, britannca, youtube, etc.

## How to use
### Britannica Scrapper
It scrapes web-pages of [britannica.com](https://www.britannica.com/) to generate the data.

```python
from britannica import Scrapper
bs = Scrapper(search_queries=['antarctica', 'america', 'continents'], max_limit=10)
bs(out_file='../scrapped_data.txt.')
```

I've made a sample `search_queries.json` that contains few keywords that could be used to scraped the pages. You can use your own, though.

```python
from britannica import searchQueries

queries = searchQueries()
print(queries())
```

### Wikipedia Scrapper
It scrapes web-pages from [wikipedia.com](https://en.wikipedia.org/) to generate the data for later uses.
It has one more feature `extra_urls=True`, this, if True will fetch new urls present on the initial query-web-pages, and will scrape those pages too.

```python
from wikipedia import WikiScraper
scrape = WikiScraper()
scrape(search_queries=["Antarctica", "Colonization", "World war"], out_file=out_file, extra_url=True)
```

I've included sample `search_queries` that can be used to scrape certain data. You're free to use your own queries.

```python
from wikipedia import WikiQueries

queries = WikiQueries()
print(queries())
```

If you're downloading XML dumps from Wikipedia eg. dump: [Dump Page for March 2024](https://dumps.wikimedia.org/wikidatawiki/20240301/). Use `xml_parser.py` to convert .xml to a .txt file containing all target urls and then run `WikiXMLScrapper()` to generate a large .txt file.

```python
from wikipedia import WikiXMLScraper

scraper = WikiXMLScraper()
url_file = 'extracted_urls.txt'
output_file = 'Datasets/wiki_110k.txt'

start_time = timeit.default_timer()
scraper.scrape_from_file(url_file, output_file, batch_size=500)
print(f"Total time taken: {timeit.default_timer() - start_time:.2f} mins")
```

### Transcripts Collector
It uses [Youtube V3 api](https://developers.google.com/youtube/v3/docs) to fetch uploaded videos by a particular channel and then generates `video_ids` which then is used to generate transcripts using [youtube-transcripts-api](https://github.com/jdepoix/youtube-transcript-api/tree/master). `max_results` can be set up to 100, not more than that.

```python
import os
api_key = os.getenv('yt_secret_key')
out_file = 'transcripts.txt'

from youtube_transcripts import TranscriptsCollector
ts = TranscriptsCollector(api_key=api_key)
ts(channel_ids=["UCb_MAhL8Thb3HJ_wPkH3gcw"], target_file=out_file, max_results=100)
```

I've included list of more than 100 YouTube channels' ids in `channel_ids.json`. You can use those or you can use according to your convinience. These `channel_ids` can generate upto 4gbs of transcripts from over ~200k videos.

It would take a lot of time though; for me, it took around ~55hrs to fetch transcripts from 167k videos.

```python
// channel_ids.json

[
  "UCb_MAhL8Thb3HJ_wPkH3gcw",
  "UCA295QVkf9O1RQ8_-s3FVXg",
  "UCpFFItkfZz1qz5PpHpqzYBw",
  ....
  "UCiMhD4jzUqG-IgPzUmmytRQ",
  "UCB0JSO6d5ysH2Mmqz5I9rIw",
  "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
]
```

Or use the `snippet.py` to import it in your code directly, check it if you want to add new channel ids, or if you're curious to see the channel names.

```python
# importing snippets

from youtube_transcripts import SampleSnippets

snippets = SampleSnippets()
print(snippets())
```

## File Structure
```
.
├── britannica
│   ├── __init__.py
│   ├── main.py
│   ├── queries.py
│   ├── requirements.txt
│   ├── search_queries.json
│   ├── URLFetcher.py
├── javascript
│   ├── customLinkFinder.js
│   ├── customSearch.js
│   ├── customWebScrapper.js
│   ├── googleCustomSearch.js
│   ├── sample.js
│   ├── webDataScrapping.js
├── run.py
│   ├── run_britannica.py
│   ├── run_transcripts.py
│   ├── run_wiki.py
├── wikipedia
│   ├── __init__.py
│   ├── fetch_urls.py
│   ├── main.py
│   ├── queries.py
│   ├── requirements.txt
│   ├── search_queries.json
├── youtube_transcripts
│   ├── __init__.py
│   ├── basic.py
│   ├── channe_ids_snippet.json
│   ├── channel_ids.json
│   ├── main.py
│   ├── requirements.txt
│   ├── snippets.py
│   ├── version2.py
├── .gitignore
├── CONTRIBUTING.md
├── LargeDataCollector.ipynb
├── LICENSE
├── README.md
├── test.py
├── wiki_extractor.py
├── xml_parser.py
```

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

Check out [CONTRIBUTING.md](https://github.com/shivendrra/web-graze/blob/main/CONTRIBUTING.md) for more details

## License
MIT License