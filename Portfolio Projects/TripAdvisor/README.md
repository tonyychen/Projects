# TripAdvisor Review Analysis
This project explores different topics such as data collection, data cleaning, data analysis, etc. The data would come from the review sections of the TripAdvisor websites.

Note: Because some data files are too large, they might not be committed.

## Here is the progress we have till now:

- ### [Scraping reviews on Arcadia National Park](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Scraper/Scraper/spiders/tripadvisor.py)
  - Using Scrapy, starting from small, we focus on scraping reviews on Arcadia National Park because I am a national park fan.
  - We grabbed JSON data that contains the reviews, the JSON data is messy so we did some preliminary cleaning using regex.
  - We then dump the JSON data into a csv file for processing.
  
- ### [Acadia Reviews Exploratory Analysis](https://nbviewer.jupyter.org/github/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Notebooks/1.%20Acadia%20Reviews%20Exploratory%20Analysis.ipynb)
  (Sorry, some Plotly graph objects might not show correctly)
  - Read the output from Scraper.
  - Parsed out JSON review data into Pandas DataFrame.
  - Explored Time-Series and Geographical distributions on the review data.
  - Finally saved the structured review data for later use.
  
- ### [Acadia Reviews Text Analysis](https://nbviewer.jupyter.org/github/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Notebooks/2.%20Acadia%20Reviews%20Text%20Analysis.ipynb)
  - Performed text analysis by parsing out individual words and plotting WordClouds. We tried to see word/topic importance in different contexts.
  - Further NLP analysis possible once we have more review data.
