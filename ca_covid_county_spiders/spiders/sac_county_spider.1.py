import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt

class SacSpider(scrapy.Spider):
    name = "sac_county"
    start_urls = [
        'https://www.saccounty.net/COVID-19/Pages/default.aspx',
    ]

    def parse(self, response):
        page = response.css('div.content').get()
        yield salt(response, {
            'content': markdownIt(page),
        })