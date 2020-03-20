import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader



class LosAngelesPageSpider(scrapy.Spider):
    name = "los_angeles_page"
    start_urls = [
        'https://lacounty.gov/covid19/frequently-asked-questions/',
        'https://lacounty.gov/covid19/children-and-families/',
        'https://lacounty.gov/covid19/consumers-businesses/',
        'https://lacounty.gov/covid19/price-gouging/',
        'https://lacounty.gov/covid19/consumers-businesses/avoiding-scams/',
        'https://lacounty.gov/covid19/consumers-businesses/for-businesses/',
        'https://lacounty.gov/covid19/consumers-businesses/for-travelers/',
        'https://lacounty.gov/covid19/utility-bill-relief/',
        'https://lacounty.gov/covid19/seniors/',
        'https://lacounty.gov/covid19/advice-for-pregnant-women/',
        'https://lacounty.gov/covid19/homelessness-and-housing/',
        'https://lacounty.gov/covid19/coping-with-stress/',
        'https://lacounty.gov/covid19/closures/',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.grve-main-content-wrapper')
        page_loader = loader.nested_css('div.grve-main-content-wrapper')
        page_loader.add_css('title', 'h1, h2, h3, h4')
        return loader.load_item()



class LosAngelesNewsSpider(scrapy.Spider):
    name = "los_angeles_news"
    start_urls = [
        'https://lacounty.gov/covid19/newsroom/',
    ]
    
    def parse(self, response):
        for item in response.css('article div.grve-post-content'):
            link = item.css('a.grve-read-more::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.grve-main-content-wrapper')
        page_loader = loader.nested_css('div.grve-main-content-wrapper')
        page_loader.add_css('title', 'h1, h2, h3, h4')
        return loader.load_item()


# Lots of PDFs on this page. Revisit when we start scraping PDFs.
# Grab the news feed for now.
class LosAngelesHealthNewsSpider(scrapy.Spider):
    name = "los_angeles_health_news"
    start_urls = [
        'http://publichealth.lacounty.gov/media/Coronavirus/',
    ]
    
    def parse(self, response):
        for item in response.xpath('//div[@class="content-padding"]//div[contains(@class, "row")][3]//p'):
            link = item.css('a::attr(href)').get()
            if link is not None:
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_xpath('content', '//table[2]')
        loader.add_css('title', 'span.contTitle2')
        return loader.load_item()