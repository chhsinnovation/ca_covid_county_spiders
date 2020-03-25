from scrapy.spiderloader import SpiderLoader
from scrapy.utils import project
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from crochet import setup, wait_for
import os

setup()

# Start sqlite3 fix
# https://stackoverflow.com/questions/52291998/unable-to-get-results-from-scrapy-on-aws-lambda
import imp
import sys
sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")
# End sqlite3 fix


def is_in_aws():
    return os.getenv('AWS_EXECUTION_ENV') is not None
    
    
@wait_for(180)
def run_spider(settings, spider):
    runner = CrawlerRunner(settings)
    deferred = runner.crawl(spider)
    return deferred


def crawl(settings={}, spider_name='all'):
    project_settings = project.get_project_settings()
    spider_loader = SpiderLoader.from_settings(project_settings)
    
    feed_uri = ""
    feed_format = "json"
    
    spider_classes = []
    
    if not spider_name.lower() == 'all':
        spider_class = spider_loader.load(spider_name)
        spider_classes.append(spider_class)
    else:
        spiders = spider_loader.list()
        for name in spiders:
            spider_class = spider_loader.load(name)
            spider_classes.append(spider_class)
    
    if is_in_aws():
        settings['HTTPCACHE_DIR'] = '/tmp'
        bucket = os.getenv('FEED_BUCKET_NAME')
        feed_uri = "s3://{}/%(name)s-%(time)s.{}".format(bucket, feed_format)
    else:
        output = os.path.join(os.getcwd(), "output")
        feed_uri = "file://{}/%(name)s-%(time)s.{}".format(output, feed_format)
    
    settings['FEED_URI'] = feed_uri
    settings['FEED_FORMAT'] = feed_format
    
    configure_logging()
    for spider in spider_classes:
        run_spider({**project_settings, **settings}, spider)