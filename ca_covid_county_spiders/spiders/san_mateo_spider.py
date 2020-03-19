import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader


class SanMateoStepsSpider(scrapy.Spider):
    name = "san_mateo_steps"
    start_urls = [
        'https://www.smcgov.org/',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.pane-12')
        loader.add_css('title', 'div.pane-12 h3')
        return loader.load_item()


 
class SanMateoNewsSpider(scrapy.Spider):
    name = "san_mateo_news"
    start_urls = [
        'https://www.smcgov.org/',
    ]
    
    def parse(self, response):
        pane = response.css('div.pane-opensanmateo-search-panel-pane-6')
        for item in pane.css('li.views-row'):
            link = item.css('a::attr(href)').get()
            if link is not None:
                yield response.follow(link, self.parse_post)
        
        next_page = pane.css('li.pager-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.main-content')
        loader.add_css('title', 'h1.title')
        return loader.load_item() 



class SanMateoShelterSpider(scrapy.Spider):
    name = "san_mateo_shelter"
    start_urls = [
        'https://www.smcgov.org/shelter-place-faqs',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#main')
        loader.add_css('title', 'h1#page-title')
        return loader.load_item()
 


class SanMateoHealthSpider(scrapy.Spider):
    name = "san_mateo_health"
    start_urls = [
        'https://www.smchealth.org/post/health-officer-statements',
        'https://www.smchealth.org/post/news-you-need',
        'https://www.smchealth.org/post/resources',
        'https://www.smchealth.org/coronavirus',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'main.page-content')
        loader.add_css('title', 'main.page-content h1')
        return loader.load_item()