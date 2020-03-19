import scrapy
from ca_covid_county_spiders.items import ContentLoader
from ca_covid_county_spiders.utils.covid import textHasCovid



class SacramentoDailySpider(scrapy.Spider):
    name = "sacramento_daily"
    start_urls = [
        'https://www.saccounty.net/news/latest-news/Pages/2020-Latest-News-Archive.aspx',
    ]

    def parse(self, response):
        for item in response.css('li.dfwp-item'):
            link = item.css('h3 a::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('title', 'div.heading h2::text')
        loader.add_css('content', 'div.article')
        return loader.load_item()



class SacramentoHealthSpider(scrapy.Spider):
    name = "sacramento_health"
    start_urls = [
        'https://dhs.saccounty.net/PUB/Pages/PUB-Home.aspx',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_value('title', 'Sacramento Public Health')
        loader.add_css('content', 'div.news')
        return loader.load_item()
    


class SacramentoPageSpider(scrapy.Spider):
    name = "sacramento_page"
    start_urls = [
        'https://www.saccounty.net/COVID-19/Pages/default.aspx',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('title', 'div.content h3')
        loader.add_css('content', 'div.content')
        return loader.load_item()