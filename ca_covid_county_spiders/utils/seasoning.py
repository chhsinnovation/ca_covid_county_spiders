from datetime import datetime

def mergeDicts(dict1, dict2): 
    dict1.update(dict2)
    return dict1

def salt(response, payload):
    combined = mergeDicts(payload, {
        'scraped_from': response.url,
        'scraped_time': datetime.now().isoformat()
    })
    return combined