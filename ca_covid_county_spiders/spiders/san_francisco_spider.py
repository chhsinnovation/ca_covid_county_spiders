import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader

# San Francisco's web presence is unique. 
# Their new site, sf.gov, is a joy to use.
# But they sometimes link out to their numerous (hundreds?) other not-so-new sites.
# Just focus on sf.gov for now. Revisit later.



class SanFranciscoPageSpider(scrapy.Spider):
    name = "san_francisco_page"
    start_urls = [
        'https://sf.gov/topics/coronavirus-covid-19',
    ]
    
    def parse(self, response):
        for item in response.css('div.sfgov-services div.sfgov-container-item'):
            link = item.css('a::attr(href)').get()
            if link is not None:
                yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'main')
        loader.add_css('title', 'h1')
        return loader.load_item()



class SanFranciscoNewsSpider(scrapy.Spider):
    name = "san_francisco_news"
    start_urls = [
        'https://sf.gov/news/topics/794',
    ]
    
    def parse(self, response):
        for item in response.css('div.news--teaser--body'):
            link = item.css('a::attr(href)').get()
            if link is not None:
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'article')
        loader.add_css('title', 'h1')
        return loader.load_item()



# Cheating here by tricking one spider into tracking two sites.
class SanFranciscoHealthPageSpider(scrapy.Spider):
    name = "san_francisco_page"
    start_urls = [
        'https://www.sfdph.org/dph/alerts/coronavirus.asp',
        'https://www.sfdph.org/dph/alerts/coronavirus-pressreleases.asp',
        'https://www.sfdph.org/dph/alerts/coronavirus-testing.asp',
        'https://www.sfcdcp.org/infectious-diseases-a-to-z/coronavirus-2019-novel-coronavirus/',
        'https://www.sfcdcp.org/infectious-diseases-a-to-z/coronavirus-2019-novel-coronavirus/coronavirus-2019-information-for-healthcare-providers/',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        # 'div#main-body' is for sfdph.org, 'article' is for sfcdcp.org.
        loader.add_css('content', 'div#main-body, article')
        loader.add_css('title', 'h1')
        return loader.load_item()