import scrapy


class TulareDailySpider(scrapy.Spider):
    name = "tulare_daily"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/tulare-county-health-report/',
    ]

    def parse(self, response):
        for update in response.css('dl'):
            yield {
                'title': update.css('dt.title a::text').get(),
                'summary': update.css('dd.summary p::text').get(),
                'href': response.urljoin(update.css('dd.readmor a::attr(href)').get()),
                'url': response.url,
            }