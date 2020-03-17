import scrapy
from ca_covid_county_spiders.utils.files import writeFiles
from ca_covid_county_spiders.utils.markdown import markdownIt

class TulareDailySpider(scrapy.Spider):
    name = "tulare_daily"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/tulare-county-health-report/',
    ]

    def parse(self, response):
        data = []
        for item in response.css('dl'):
            parsed_item = {
                'title': item.css('dt.title a::text').get(),
                'content': item.css('dd.summary p::text').get(),
                'links_to': response.urljoin(item.css('dd.readmore a::attr(href)').get()),
                'scraped_at': response.url,
            }
            data.append(dict(parsed_item))
            yield parsed_item
        writeFiles(response.body, data, self.name)