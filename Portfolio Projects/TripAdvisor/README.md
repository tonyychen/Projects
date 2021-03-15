# TripAdvisor Review Analysis
This project explores different topics such as data collection, data cleaning, data analysis, etc. The data would come from the review sections of the TripAdvisor websites.

Note: Because some data files are too large, they might not be committed.

## Here is the progress we have till now:

- ### [Scraping reviews on Acadia National Park](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Scraper/Scraper/spiders/tripadvisor.py)
  - Using Scrapy, starting from small, we focus on scraping reviews on Acadia National Park because I am a national park fan.
  - We grabbed JSON data that contains the reviews, the JSON data is messy so we did some preliminary cleaning using regex in the [pipeline](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Scraper/Scraper/pipelines.py).
  - We then dump the JSON data into a JSON file for processing.
  
- ### [Acadia Reviews Exploratory Analysis](https://nbviewer.jupyter.org/github/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Notebooks/1.%20Acadia%20Reviews%20Exploratory%20Analysis.ipynb)
  (Sorry, some Plotly graph objects might not show correctly)
  - Load the JSON output from Scraper.
  - Parsed out JSON review data into Pandas DataFrame.
  - Explored Time-Series and Geographical distributions on the review data.
  - Finally saved the structured review data to CSV for later use.
  
- ### [Acadia Reviews Text Analysis](https://nbviewer.jupyter.org/github/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Notebooks/2.%20Acadia%20Reviews%20Text%20Analysis.ipynb)
  - Performed text analysis by parsing out individual words and plotting WordClouds. We tried to see word/topic importance in different contexts.
  - Further NLP analysis possible once we have more review data.

- ### [ALL National Park Reviews Exploratory Analysis]()
  - More Data: Exploratory analysis on 45+ national parks
  - Fetch Data directly from Azure SQL DB
  - Explored Time-Series and Geographical distributions on the review data.
  - Number of Reviews/Average Ratings across different national parks


## Time Fragments:

#### 2020-11-12: Allow feed export to Amazon S3
![S3 Snapshot](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Snapshots/S3%20Snapshot.PNG)

#### 2020-11-18: Initiated a Azure Data Factory Pipeline to move the JSON files from S3 to Azure Data Lake Gen2

#### 2020-12-01: Import JSON files from Azure Data Lake Gen2 to Azure SQL DB and store in a table called Reviews; supports incremental import
![SELECT Reviews Snapshot](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Snapshots/SELECT%20Reviews%20Snapshot.PNG)

#### 2020-12-14: Scraped TripAdvisor reviews across all available National Parks (see [nationalpark_urls.py](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Scraper/Scraper/spiders/nationalpark_urls.py)) and used established pipeline to import into Azure SQL DB
![SELECT All Reviews Count Snapshot](https://github.com/tonyychen/Projects/blob/master/Portfolio%20Projects/TripAdvisor/Snapshots/SELECT%20All%20Reviews%20Count%20Snapshot.PNG)