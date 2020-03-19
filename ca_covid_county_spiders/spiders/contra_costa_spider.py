import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader




class ContraCostaPageSpider(scrapy.Spider):
    name = "contra_costa_page"
    start_urls = [
        'https://www.contracosta.ca.gov/',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#cceb7e72db-b12d-4887-8946-387a18f7f068')
        loader.add_css('title', 'div#cceb7e72db-b12d-4887-8946-387a18f7f068 h1.headline span span::text')
        return loader.load_item()

  

class ContraCostaPostSpider(scrapy.Spider):
    name = "contra_costa_post"
    start_urls = [
        'https://www.contracosta.ca.gov/CivicAlerts.aspx?CID=-1&searchTerms=&sort=date',
    ]

    def parse(self, response):
        for item in response.css('div.item'):
            link = item.css('a.more::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.content')
        loader.add_css('title', 'div.item h3::text')
        return loader.load_item()



class ContraCostaHealthPostSpider(scrapy.Spider):
    name = "contra_costa_health_post"
    start_urls = [
        'https://cchealth.org/press-releases/',
    ]

    def parse(self, response):
        first_post = response.xpath('//article/div[1]/div/div[2]')
        link = first_post.css('a::attr(href)').get()
        if link is not None and textHasCovid(first_post.get()):
            yield response.follow(link, self.parse_post)
        
        for item in response.css('tr'):
            link = item.css('a::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'article#content_begins')
        loader.add_css('title', 'article#content_begins h2::text')
        return loader.load_item()



class ContraCostaCovidPageSpider(scrapy.Spider):
    name = "contra_costa_covid_page"
    start_urls = [
        'https://www.coronavirus.cchealth.org/prevention',
        'https://www.coronavirus.cchealth.org/if-you-are-sick',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'main#PAGES_CONTAINER')
        loader.add_css('title', 'title::text')
        return loader.load_item()