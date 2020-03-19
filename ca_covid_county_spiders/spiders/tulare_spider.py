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
            yield salt(self, response, {
                'title': item.css('dt.title a::text').get(),
                'content': item.css('dd.summary p::text').get(),
                'links_to': response.urljoin(item.css('dd.readmore a::attr(href)').get()),
            })



class TularePageSpider(scrapy.Spider):
    name = "tulare_page"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/',
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/what-you-should-know/',
    ]

    def parse(self, response):
        page = response.css('article div.mura-region-local').get()
        yield salt(self, response, {
            'content': markdownIt(page),
        })