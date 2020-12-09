import scrapy
from . import nationalpark_urls

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = nationalpark_urls.park_urls


    def parse(self, response):
        js = response.xpath(
            '//script[starts-with(text(), "window.__WEB_CONTEXT__")]/text()').get()

        # output json
        yield {
            'JS': js
        }

        #Pagination (next page)
        next_page = response.xpath('//a[@class="ui_button nav next primary "]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


