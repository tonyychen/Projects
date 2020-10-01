import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html']

    def parse(self, response):
        for review in response.xpath('//q[@class="IRsGHoPm"]/span/text()'):
            yield {
                'text': review.get()
            }
