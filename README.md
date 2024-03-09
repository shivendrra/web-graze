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
│   ├── TestDataCollector.py
│   ├── channel_ids.json
│   ├── channe_ids_snippet.json
│   ├── requirements.txt
│   ├── transcriptCollector.py
│   ├── YTFineTuneDataCollector.py
│   ├── videoUrls.json
├── .env
├── .gitignore
├── README.md
├── test.py
```
## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
None for now!!