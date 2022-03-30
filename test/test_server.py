import requests

URL = 'http://localhost'
PORT = 7008
HEADER = {'Content-type': 'application/json'}

def getRq():
        x = requests.get(URL+':'+str(PORT)+'/app', headers=HEADER)
        print(x.json())

def postRq(rq):
        x = requests.post(URL+':'+str(PORT)+'/app', json=rq, headers=HEADER)
        print(x.json())

getRq()

postRq({'id':'123'})