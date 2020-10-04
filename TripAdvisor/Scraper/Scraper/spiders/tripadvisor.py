import scrapy
import re

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html#REVIEWS']

    def parse(self, response):
        js = response.xpath('//script[starts-with(text(), "window.__WEB_CONTEXT__")]/text()').get()
        #remove start
        js = re.sub(r'^window\.__WEB_CONTEXT__\s*=\s*{', r'{', js)
        #remove end
        js = re.sub(r'};\(this\.\$WP.+$', r'}', js)
        #double-quote "pageManifest"
        js = js.replace('pageManifest', '"pageManifest"')

        #output json
        with open('testfile.json', 'w') as f:
            f.write(js)