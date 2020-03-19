import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader


class PlacerNewsSpider(scrapy.Spider):
    name = "placer_news"
    start_urls = [
        'https://www.placer.ca.gov/CivicAlerts.aspx?CID=13,5&sort=date',
    ]
    
    def parse(self, response):
        for item in response.css('div.contentMain div.item'):
            link = item.css('a.Hyperlink::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#page')
        page_loader = loader.nested_css('div#page')
        page_loader.add_css('title', 'h1, h2, h3, h4')
        return loader.load_item()



class PlacerPageSpider(scrapy.Spider):
    name = "placer_page"
    start_urls = [
        'https://www.placer.ca.gov/6448/Cases-in-Placer',
        'https://www.placer.ca.gov/6449/Guidance',
        'https://www.placer.ca.gov/6451/Healthcare',
        'https://www.placer.ca.gov/6452/Resources',
    ]

    def parse(self, response):
        # Repeated from the Placer News spider, for now.
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#page')
        page_loader = loader.nested_css('div#page')
        page_loader.add_css('title', 'h1, h2, h3, h4')
        return loader.load_item()



class PlacerFAQSpider(scrapy.Spider):
    name = "placer_faq"
    start_urls = [
        'https://www.placer.ca.gov/Faq.aspx?TID=210',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div.contentMain')
        loader.add_value('title', 'COVID-19 FAQ')
        return loader.load_item()