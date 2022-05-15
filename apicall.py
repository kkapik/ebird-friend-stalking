#!/usr/bin/env python3

import requests
from ebird.api import  get_checklist, get_taxonomy


def get_daily(api_key, loc_code, day):

    url = "https://api.ebird.org/v2/product/lists/"+ loc_code +'/'+day[2]+'/'+day[1]+'/'+day[0]+"?maxResults=200"
    payload={}
    headers = {'X-eBirdApiToken': api_key}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_name(api_key, code, locale):
    url = "https://api.ebird.org/v2/ref/taxonomy/ebird?species="+ code +"&version=2019&locale="+locale

    payload={    }
    headers = {
      'X-eBirdApiToken': api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    text= response.text
    list=text.split(',')
    return list[15]

def get_species(api_key, dict, locale):
    jsonstr = get_checklist(api_key, dict["listID"])
    list = jsonstr['obs']
    speciesList=[]
    for i in list:
        speciesList.append(i['speciesCode'])

    return {'auteur':dict["auteur"], 'speciesList': speciesList}


def speciesOTD(codes):
    codeList=[]
    for i in codes:
        for j in i['speciesList']:
            if not(j in codeList):
                codeList.append(j)
    return codeList

def code_dict(api_key, list, locale):
    dict = {}
    for i in list:
        name=get_name(api_key, i, locale)
        dict[i]=name
    return dict
