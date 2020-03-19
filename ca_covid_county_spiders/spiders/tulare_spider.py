import scrapy
from ca_covid_county_spiders.items import ContentLoader
from ca_covid_county_spiders.utils.covid import textHasCovid




class TulareDailySpider(scrapy.Spider):
    name = "tulare_daily"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/tulare-county-health-report/',
    ]
            
    def parse(self, response):
        for item in response.css('dl'):
            link = item.css('dt.title a::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('title', 'header h2::text')
        loader.add_css('content', 'article#main')
        return loader.load_item()



class TularePageSpider(scrapy.Spider):
    name = "tulare_page"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/',
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/what-you-should-know/',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('title', 'article header h2::text')
        loader.add_css('content', 'article div.mura-region-local')
        return loader.load_item()