import requests
import json
import re

MY_IP = 'localhost'
LIB = {
    'getversion': {"jsonrpc": "2.0", "method": "getversion", "params": [], "id": 3},
    'getblockcount': {"jsonrpc": "2.0", "method": "getblockcount", "params": [], "id": 0}
}
HEIGHT = 0
CLI_VERSION = "0"


def postNode(query):
    res = requests.post('http://{0}:10332'.format(MY_IP), data = json.dumps(query), timeout=5)
    return res.json()['result']


try:  
    CLI_VERSION = postNode(LIB['getversion'])['useragent']
    CLI_VERSION = re.sub(r'[a-zA-Z//:]+', '', CLI_VERSION)

    HEIGHT = int(postNode(LIB['getblockcount']))

    with open('state.json', 'wb') as stateFile:
       json.dump({'version': CLI_VERSION, 'height': HEIGHT}, stateFile, indent=4)
except:
    pass
