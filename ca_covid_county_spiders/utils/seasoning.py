import hashlib
from datetime import datetime


def mergeDicts(dict1, dict2): 
    dict1.update(dict2)
    return dict1

def salt(spider, response, payload):
    combined = mergeDicts({
        'scraped_by': spider.name,
        'scraped_hash': hashlib.md5(response.body).hexdigest(),
        'scraped_from': response.url,
        'scraped_time': datetime.now().isoformat()
    }, payload)
    return combined