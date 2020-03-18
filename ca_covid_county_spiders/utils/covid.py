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