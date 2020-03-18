import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt
from ca_covid_county_spiders.utils.covid import hasCovid

class SacCountyDailySpider(scrapy.Spider):
    name = "sac_county_daily"
    start_urls = [
        'https://www.saccounty.net/news/latest-news/Pages/2020-Latest-News-Archive.aspx',
    ]

    def parse(self, response):
        for link in response.css('li.dfwp-item h3 a'):
            yield response.follow(link, self.parse_post)
    
    def parse_post(self, response):
        page = response.css('div.article').get()
        data = salt(response, {
            'title': response.css('div.heading h2::text').get(),
            'content': markdownIt(page),
        })
        if hasCovid(data):
            yield data
        else:
            return
        