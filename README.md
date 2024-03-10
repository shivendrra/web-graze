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

### Transcripts Collector
It uses [Youtube V3 api](https://developers.google.com/youtube/v3/docs) to fetch uploaded videos by a particular channel and then generates `video_ids` which then is used to generate transcripts using [youtube-transcripts-api](https://github.com/jdepoix/youtube-transcript-api/tree/master).

```python
import os
api_key = os.getenv('yt_secret_key')
out_file = 'transcripts.txt'

from youtube_transcripts import TranscriptsCollector
ts = TranscriptsCollector(api_key=api_key)
ts(channel_ids=["UCb_MAhL8Thb3HJ_wPkH3gcw"], target_file=out_file)
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
├── youtube_transcripts
│   ├── __init__.py
│   ├── basic.py
│   ├── channe_ids_snippet.json
│   ├── channel_ids.json
│   ├── main.py
│   ├── requirements.txt
│   ├── snippets.py
│   ├── version2.py
├── .env
├── .gitignore
├── CONTRIBUTING.md
├── LargeDataCollector.ipynb
├── LICENSE
├── README.md
├── test.py
```

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

Check out [CONTRIBUTING.md](https://github.com/shivendrra/web-graze/blob/main/CONTRIBUTING.md) for more details

## License
None for now!!