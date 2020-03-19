import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt
from ca_covid_county_spiders.utils.covid import dataHasCovid



class SacramentoDailySpider(scrapy.Spider):
    name = "sacramento_daily"
    start_urls = [
        'https://www.saccounty.net/news/latest-news/Pages/2020-Latest-News-Archive.aspx',
    ]

    def parse(self, response):
        for link in response.css('li.dfwp-item h3 a'):
            yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        page = response.css('div.article').get()
        data = salt(self, response, {
            'title': response.css('div.heading h2::text').get(),
            'content': markdownIt(page),
        })
        if dataHasCovid(data):
            yield data
        else:
            return



class SacramentoHealthSpider(scrapy.Spider):
    name = "sacramento_health"
    start_urls = [
        'https://dhs.saccounty.net/PUB/Pages/PUB-Home.aspx',
    ]

    def parse(self, response):
        page = response.css('.col-sm-8').get()
        yield salt(self, response, {
            'content': markdownIt(page),
        })
    


class SacramentoPageSpider(scrapy.Spider):
    name = "sacramento_page"
    start_urls = [
        'https://www.saccounty.net/COVID-19/Pages/default.aspx',
    ]

    def parse(self, response):
        page = response.css('div.content').get()
        yield salt(self, response, {
            'content': markdownIt(page),
        })