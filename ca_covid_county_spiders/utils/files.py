from datetime import datetime
import json

def filebase(name):
    now = datetime.now()
    return 'output/' + name + '_' + now.strftime("%Y%m%d_%H%M%S")

def writeHTML(html, name):
    filebase_str = filebase(name)
    with open(filebase_str + '.html', 'wb') as f:
        f.write(html)

def writeJSON(data, name):
    filebase_str = filebase(name)
    with open(filebase_str + '.json', 'w') as f:
        f.write(json.dumps(data))

def writeFiles(html, data, name):
    writeHTML(html, name)
    writeJSON(data, name)