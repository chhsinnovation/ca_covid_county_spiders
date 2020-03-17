import scrapy

class TulareDailySpider(scrapy.Spider):
    name = "tulare_daily"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/tulare-county-health-report/',
    ]

    def parse(self, response):
        for item in response.css('dl'):
            yield {
                'title': item.css('dt.title a::text').get(),
                'content': item.css('dd.summary p::text').get(),
                'links_to': response.urljoin(item.css('dd.readmore a::attr(href)').get()),
                'scraped_at': response.url,
            }