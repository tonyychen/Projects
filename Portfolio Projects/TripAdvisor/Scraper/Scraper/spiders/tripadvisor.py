import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g43447-d12659479-Reviews-Voyageurs_National_Park-Ray_Minnesota.html'] #['https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html#REVIEWS']

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


