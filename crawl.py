from scrapy.spiderloader import SpiderLoader
from scrapy.utils import project
from scrapy.crawler import CrawlerProcess

settings = project.get_project_settings()

spider_loader = SpiderLoader.from_settings(settings)
spiders = spider_loader.list()
spider_classes = [spider_loader.load(name) for name in spiders]

process = CrawlerProcess(settings=settings)
for spider in spider_classes:
    process.crawl(spider)
process.start()