import scrapy
import html2text
from ca_covid_county_spiders.utils.markdown import markdownIt

class TularePageSpider(scrapy.Spider):
    name = "tulare_page"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/',
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/what-you-should-know/',
    ]

    def parse(self, response):
        page = response.css('article div.mura-region-local').get()
        yield {
            'content': markdownIt(page),
            'scraped_at': response.url,
        }