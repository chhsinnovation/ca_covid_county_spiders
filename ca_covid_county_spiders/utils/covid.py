keywords = [
    'COVID-19',
    'COVID19',
    'COVID',
    'covid-19',
    'covid19',
    'covid',
    'Coronavirus',
    'coronavirus',
    'corona virus',
    'Corona',
    'corona',
    'SARS-CoV-2',
    'SARSCov2',
    'SARS CoV 2',
    'social distancing',
    'distancing',
    'community spread',
    'isolation',
    'shelter at home',
    'shelter in place',
    'shelter',
]

def searchDict(myDict, term):
    findings = []
    for key, value in myDict.items():
        if term in value:
            findings.append(key)
    return findings

def dataHasCovid(payload):
    findings = []
    for keyword in keywords:
        query = searchDict(payload, keyword)
        if query:
            findings = findings + query
    if findings:
        return True
    else: 
        return False
        
def textHasCovid(string):
    findings = []
    for keyword in keywords:
        if keyword in string:
            findings.append(keyword)
    if findings:
        return True
    else: 
        return False
    