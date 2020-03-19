import scrapy
from ca_covid_county_spiders.utils.covid import textHasCovid
from ca_covid_county_spiders.items import ContentLoader


class SantaClaraNewsSpider(scrapy.Spider):
    name = "santa_clara_news"
    start_urls = [
        'https://www.sccgov.org/sites/opa/Pages/default.aspx',
    ]
    
    def parse(self, response):
        for item in response.css('div.sccgov-alert-item'):
            link = item.css('a::attr(href)').get()
            if link is not None and textHasCovid(item.get()):
                yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#scc-portal-article-content-container')
        loader.add_css('title', 'div#scc-portal-article-content-container h1')
        return loader.load_item()



class SantaClaraHealthSpider(scrapy.Spider):
    name = "santa_clara_health"
    start_urls = [
        'https://www.sccgov.org/sites/phd/DiseaseInformation/novel-coronavirus/Pages/home.aspx',
        'https://www.sccgov.org/sites/phd/news/Pages/covid-19-call-211.aspx',
        'https://www.sccgov.org/sites/phd/DiseaseInformation/novel-coronavirus/Pages/frequently-asked-questions.aspx',
        'https://www.sccgov.org/sites/phd/DiseaseInformation/novel-coronavirus/Pages/resources-public-info-outearch.aspx',
        'https://www.sccgov.org/sites/phd-p/Diseases/novel-coronavirus/Pages/home.aspx',
        'https://www.sccgov.org/sites/opa/opa/covid19/Pages/home.aspx',
    ]
    
    def parse(self, response):
        loader = ContentLoader(response=response)
        loader.add_css('content', 'div#scc-portal-article-content-container')
        loader.add_css('title', 'div#scc-portal-article-content-container h1')
        return loader.load_item()


