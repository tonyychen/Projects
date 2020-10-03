import scrapy
from scrapy_splash import SplashRequest

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g60709-d12785836-Reviews-Acadia_National_Park-Bar_Harbor_Mount_Desert_Island_Maine.html']

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false

        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        
        splash:set_viewport_full()
        return splash.html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url = self.start_urls[0], callback=self.parse, endpoint='execute', args={
            'lua_source': self.script
        })

    def parse(self, response):
        with open('testfile.txt', 'wb') as f:
            f.write(response.body)
