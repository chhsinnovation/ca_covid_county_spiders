from datetime import datetime

def mergeDicts(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

def salt(response, payload):
    combined = mergeDicts(payload, {
        'scraped_from': response.url,
        'scraped_time': datetime.now().isoformat()
    })
    return combined