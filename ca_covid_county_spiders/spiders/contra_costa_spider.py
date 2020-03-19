import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt
from ca_covid_county_spiders.utils.covid import dataHasCovid, textHasCovid



class ContraCostaPageSpider(scrapy.Spider):
    name = "contra_costa_page"
    start_urls = [
        'https://www.contracosta.ca.gov/',
    ]

    def parse(self, response):
        blurb = response.css('div#cceb7e72db-b12d-4887-8946-387a18f7f068')
        data = salt(self, response, {
            'title': blurb.css('h1.headline span span::text').get(),
            'content': markdownIt(blurb.get()),
        })
        if dataHasCovid(data):
            yield data
        else:
            return

  

class ContraCostaPostSpider(scrapy.Spider):
    name = "contra_costa_post"
    start_urls = [
        'https://www.contracosta.ca.gov/CivicAlerts.aspx?CID=-1&searchTerms=&sort=date',
    ]

    def parse(self, response):
        for item in response.css('div.item'):
            link = item.css('a.more::attr(href)').get()
            if link is not None:
                if textHasCovid(item.get()):
                    yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        page = response.css('div.content').get()
        data = salt(self, response, {
            'title': response.css('div.item h3::text').get(),
            'content': markdownIt(page),
        })
        if dataHasCovid(data):
            yield data
        else:
            return



class ContraCostaHealthPostSpider(scrapy.Spider):
    name = "contra_costa_health_post"
    start_urls = [
        'https://cchealth.org/press-releases/',
    ]

    def parse(self, response):
        first_post = response.xpath('//article/div[1]/div/div[2]')
        link = first_post.css('a::attr(href)').get()
        if link is not None:
            if textHasCovid(first_post.get()):
                yield response.follow(link, self.parse_post)
        
        for item in response.css('tr'):
            link = item.css('a::attr(href)').get()
            if link is not None:
                if textHasCovid(item.get()):
                    yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        page = response.css('article#content_begins').get()
        data = salt(self, response, {
            'title': response.css('article#content_begins h2::text').get(),
            'content': markdownIt(page),
        })
        if dataHasCovid(data):
            yield data
        else:
            return



class ContraCostaCovidPageSpider(scrapy.Spider):
    name = "contra_costa_covid_page"
    start_urls = [
        'https://www.coronavirus.cchealth.org/prevention',
        'https://www.coronavirus.cchealth.org/if-you-are-sick',
    ]

    def parse(self, response):
        page = response.css('main#PAGES_CONTAINER').get()
        yield salt(self, response, {
            'title': response.css('title::text').get(),
            'content': markdownIt(page),
        })