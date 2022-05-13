import requests
import json
from ebird.api import  get_checklist, get_taxonomy


api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.


def get_daily(loc_code, date):

    url = "https://api.ebird.org/v2/product/lists/"+ loc_code +'/'+date[2]+'/'+date[1]+'/'+date[0]+"?maxResults=200"
    payload={}
    headers = {'X-eBirdApiToken': api_key}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def get_name(code):
    url = "https://api.ebird.org/v2/ref/taxonomy/ebird?species="+ code +"&version=2019&locale=fr"

    payload={    }
    headers = {
      'X-eBirdApiToken': api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    text= response.text
    list=text.split(',')
    return list[15]

def get_species(dict):
    jsonstr = get_checklist(api_key, dict["listID"])
    list = jsonstr['obs']
    specieslist=[]
    for i in list:
        specieslist.append(get_name(i['speciesCode']))

    return {'auteur':dict["auteur"], 'speciesList': specieslist}


def main(loc,date):
    dateL = date.split('/')
    feed = (get_daily(loc, dateL))
    js_feed = json.loads(feed)
    checklists=[]
    for c in js_feed:
        if c["userDisplayName"] in my_friends:
            checklists.append({'auteur':c["userDisplayName"],'listID':c["subID"]})
    if checklists == []:
        print("No observation for your friends to day! :(")
        return None
    result=[]
    for i in checklists:
        result.append(get_species(i))

    for k in result:
        str= k['auteur'] + ' have seen: '
        for l in k['speciesList']:
            str += l + ', '
        str = str[:-2]+ '.\n'
        print(str)
    return None


if __name__ == '__main__':
    print('Zone?')
    location = input()
    print('Date? ((d)d/(m)m/yyyy)')
    datum = input()
    print('Language?')
    locale = input()
    r = main(location, datum)
