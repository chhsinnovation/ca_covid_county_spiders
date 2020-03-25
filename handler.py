import json
import sys
from ca_covid_county_spiders.crawl import crawl

# Serverless smoke test.
def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

  

def scrape(event={}, context={}):
    crawl(**event)
    


if __name__ == "__main__":
    event = {}
    
    try:
        event['spider_name'] = sys.argv[1]
    except IndexError:
        event['spider_name'] = 'all'
        
    try:
        event['settings'] = json.loads(sys.argv[2])
    except IndexError:
        event['settings'] = {}
        
    scrape(event)