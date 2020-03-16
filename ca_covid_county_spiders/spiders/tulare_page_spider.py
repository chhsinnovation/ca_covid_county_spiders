import scrapy
import html2text

textGen = html2text.HTML2Text()
textGen.body_width = 0

class TularePageSpider(scrapy.Spider):
    name = "tulare_page"
    start_urls = [
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/',
        'https://tchhsa.org/eng/index.cfm/public-health/covid-19-updates-novel-coronavirus/what-you-should-know/',
    ]

    def parse(self, response):
        page = response.css('article div.mura-region-local').get()
        md = textGen.handle(page)
        yield {
            'text': md,
            'url': response.url,
        }