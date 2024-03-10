# data-collection

## Introduction
this repo contains codes that would help you to scrape data from various sites on the internet like wikipedia, britannca, youtube, etc.

## How to use
### Britannica Scrapper
```python
from britannica import Scrapper
bs = Scrapper(search_queries=['antarctica', 'america', 'continents'], max_limit=10)
bs(out_file='../scrapped_data.txt.')
```

### Transcripts Collector
-- in progeress

```python
import os
api_key = os.getenv('yt_secret_key')
out_file = 'transcripts.txt'

from youtube_transcripts import TranscriptsCollector
ts = TranscriptsCollector(api_key=api_key)
ts(channel_ids=["UCb_MAhL8Thb3HJ_wPkH3gcw"], target_file=out_file)
```

I've included list of more than 100 YouTube channels' ids in `channel_ids.json`. You can use those or you can use according to your convinience. These `channel_ids` can generate upto 4gbs of transcripts from over ~200k videos.

```json
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

## File Structure
```
.
├── britannica
│   ├── __init__.py
│   ├── URLFetcher.py
│   ├── requirements.txt
│   ├── main.py
│   ├── search_queries.json
├── javascript
│   ├── customLinkFinder.js
│   ├── customSearch.js
│   ├── customWebScrapper.js
│   ├── googleCustomSearch.js
│   ├── sample.js
│   ├── webDataScrapping.js
├── Transcript Collection
│   ├── __init__.py
│   ├── basic.py
│   ├── channel_ids.json
│   ├── channe_ids_snippet.json
│   ├── requirements.txt
│   ├── main.py
│   ├── version2.py
├── .env
├── .gitignore
├── README.md
├── test.py
```
## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
None for now!!