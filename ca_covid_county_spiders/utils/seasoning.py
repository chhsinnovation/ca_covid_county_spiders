from datetime import datetime

def searchDict(myDict, term):
    findings = []
    for key, value in myDict.items():
        if term in value:
            findings.append(key)
    return findings

def hasCovid(payload):
    keywords = [
        'COVID-19',
        'COVID19',
        'COVID',
        'coronavirus',
        'corona virus',
        'corona',
        'SARS-CoV-2',
        'SARSCov2',
        'SARS CoV 2',
    ]
    findings = []
    for keyword in keywords:
        query = searchDict(payload, keyword)
        if query:
            findings = findings + query
    if findings:
        return True
    else: 
        return False
                
def mergeDicts(dict1, dict2): 
    dict1.update(dict2)
    return dict1

def salt(response, payload):
    combined = mergeDicts(payload, {
        'scraped_from': response.url,
        'scraped_time': datetime.now().isoformat()
    })
    return combined