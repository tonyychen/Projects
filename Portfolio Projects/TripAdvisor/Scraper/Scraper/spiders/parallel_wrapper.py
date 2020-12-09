#Add module dir Scraper
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))



import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from tripadvisor import TripadvisorSpider
import settings as my_settings

settings = get_project_settings()
settings.setmodule(my_settings)


def MakeCrawlRunner(s3_link, settings):
    settings.set('FEEDS', {s3_link:{
    'format': 'json'
    }})
    return CrawlerRunner(settings)

configure_logging()
runner = MakeCrawlRunner('s3://tonyychen-tripadvisor/All_Reviews/Voyageor_Reviews.json', settings)
runner.crawl(TripadvisorSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run() # the script will block here until all crawling jobs are finished