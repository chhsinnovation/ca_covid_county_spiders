import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt

class SacHealthSpider(scrapy.Spider):
    name = "sac_county_health"
    start_urls = [
        'https://dhs.saccounty.net/PUB/Pages/PUB-Home.aspx',
    ]

    def parse(self, response):
        page = response.css('.col-sm-8').get()
        yield salt(response, {
            'content': markdownIt(page),
        })