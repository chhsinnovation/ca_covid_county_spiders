import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader


class ExamplePageSpider(scrapy.Spider):
    
    # Name the spider. This is what you'll plug into the terminal for crawling.
    # Ex.: scrapy crawl example_page
    name = "example_page"
    
    # Provide URLs to crawl.
    start_urls = [
        'https://www.example.com/page/1',
        'https://www.example.com/page/2',
    ]


    # Scraping instructions for each page.
    def parse(self, response):
        
        # The ContentLoader line always stays the same.
        loader = ContentLoader(response=response)
        
        # We need to scrape content and title.
        # Supply CSS selectors corresponding to content and title on the page(s).
        loader.add_css('content', 'div#bigContentContainer')
        loader.add_css('title', 'div#bigContentContainer h1')
        
        # The loader.load_itemm() line always stays the same.
        return loader.load_item()
