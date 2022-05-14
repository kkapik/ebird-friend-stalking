#!/usr/bin/env python3

import json, datetime
import apicall as eb

api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.

def main(loc,day):
    dateL=[]
    if day == "":
        current_time = datetime.datetime.now()
        dateL = [str(current_time.day)] + [str(current_time.month)] + [str(current_time.year)]
    else:
        dateL = day.split('/')
    feed = (eb.get_daily(api_key, loc, dateL))
    js_feed = json.loads(feed)
    checklists=[]
    print('\nChecing the checklist feed for the region ...')
    for c in js_feed:
        if c["userDisplayName"] in myfriends:
            checklists.append({'auteur':c["userDisplayName"],'listID':c["subID"]})
    if checklists == []:
        print("No observation for your friends to day! :(")
        return None
    result=[]
    print('Getting the species ...')
    for i in checklists:
        result.append(eb.get_species(api_key, i, locale))
    print('Preparing the result ...')
    for j in result:
        for l in result[result.index(j):]:
            if j != l:
                if j['auteur'] == l['auteur']:
                    j['speciesList'] = list(set(j['speciesList']+l['speciesList']))
                    result.pop(result.index(l))
    print('\n')
    for k in result:
        out= k['auteur'] + ' have seen: '
        for l in k['speciesList']:
            out += l + ', '
        out = out[:-2]+ '.\n'
        print(out)
    return None


if __name__ == '__main__':
    print('Zone?')
    location = input()
    if location == "":
        print("Please enter a location")
        location  =input()
    print('Date? ((d)d/(m)m/yyyy)')
    datum = input()
    print('Language? (default = en)')
    locale = input()
    if locale == "":
        locale = 'en'
    r = main(location, datum)
