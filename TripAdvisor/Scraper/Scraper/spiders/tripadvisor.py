import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com/']
    start_urls = ['http://https://www.tripadvisor.com//']

    def parse(self, response):
        pass