import scrapy
import re
import json


class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html#REVIEWS']

    def parse(self, response):
        js = response.xpath(
            '//script[starts-with(text(), "window.__WEB_CONTEXT__")]/text()').get()
        # clean up start
        js = re.sub(r'^window\.__WEB_CONTEXT__\s*=\s*{', r'{', js)
        # clean up end
        js = re.sub(r'};\(this\.\$WP.+$', r'}', js)
        # add double-quote to "pageManifest" to make it a key
        js = js.replace('pageManifest', '"pageManifest"')

        # only get the part where key = "reviewListPage", which contains review info
        js = json.loads(js)
        js = self.json_extract(js, 'reviewListPage')[0] #only 1 "reviewListPage" should exist

        # output json
        yield {
            'Review_JSON': js
        }

        #Pagination (next page)
        next_page = response.xpath('//a[@class="ui_button nav next primary "]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def json_extract(self, obj, key):
        """Extract nested values from a JSON tree."""
        """Recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == key:
                        arr.append(v)
                        
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values
