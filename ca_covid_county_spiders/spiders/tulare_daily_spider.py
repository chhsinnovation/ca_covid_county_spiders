import scrapy
from ca_covid_county_spiders.utils.markdown import markdownIt
from ca_covid_county_spiders.utils.seasoning import salt

class TulareDailySpider(scrapy.Spider):
    name = "tulare_daily"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/tulare-county-health-report/',
    ]

    def parse(self, response):
        for item in response.css('dl'):
            yield salt(response, {
                'title': item.css('dt.title a::text').get(),
                'content': item.css('dd.summary p::text').get(),
                'links_to': response.urljoin(item.css('dd.readmore a::attr(href)').get()),
            })