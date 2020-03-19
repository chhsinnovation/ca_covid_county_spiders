import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader




class SolanoNewsSpider(scrapy.Spider):
    name = "solano_news"
    start_urls = [
        'https://www.solanocounty.com/news/default.asp',
    ]
    
    def parse(self, response):
        for item in response.xpath('//div[@class="vpadcontentdiv"]/table[1]/tr'):
            link = item.css('a.newsheader::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.vpadcontentdiv')
        loader.add_css('title', 'div#newsdetails h2::text')
        return loader.load_item()



class SolanoHealthSpider(scrapy.Spider):
    name = "solano_health"
    start_urls = [
        'http://www.solanocounty.com/depts/ph/ncov.asp',
    ]

    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_xpath('content', '//table[@class="content"]/tr[1]/td[@class="col2"]')
        loader.add_xpath('title', '//table[@class="content"]/tr[1]/td[@class="col2"]//font[1]/text()')
        return loader.load_item()