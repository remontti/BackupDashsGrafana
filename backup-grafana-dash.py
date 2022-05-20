#!/usr/bin/python3
import requests
import json
import urllib3
urllib3.disable_warnings()

server = 'https://grafana.remontti.com.br'
api_token = '6n1teKM4QklfADUHSRgtdE63pMwpFgciuAgqdlejHK1dodEGYEsKsdLkuL1vR4Skw6na3envxmUsjojq'
headers = {
    "Authorization": "Bearer " + api_token
}


def search():
    url = server + "/api/search"
    content = requests.get(url=url, headers=headers, verify=False)
    return content.json()


def gerarJson(nome, dashboardJson):
    with open(nome, 'w') as json_file:
        json.dump(dashboardJson, json_file, indent=4)
        #print('Dashboard salva com sucesso >> ' + nome)


for dash in search():
    uid = dash['uid']
    nome = dash['title'] + '.json'
    url = server + '/api/dashboards/uid/' + uid
    result = requests.get(url=url, headers=headers, verify=False).json()
    dashboardJson = result['dashboard']
    gerarJson(nome, dashboardJson)
