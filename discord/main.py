#!usr/bin/env python3

import json, datetime
import apicall as eb
import discord_notify as dn

api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.

def main(loc,day):
    dateL=[]
    if day == "":
        current_time = datetime.datetime.now()
        dateL = [str(current_time.day-1)] + [str(current_time.month)] + [str(current_time.year)]
    else:
        dateL = day.split('/')
    feed = (eb.get_daily(api_key, loc, dateL))
    js_feed = json.loads(feed)
    checklists=[]
    for c in js_feed:
        if c["userDisplayName"] in myfriends:
            checklists.append({'auteur':c["userDisplayName"],'listID':c["subID"]})
    if checklists == []:
        return "Pas d'observation pour aujourd'hui"

    codes=[]
    for i in checklists:
        codes.append(eb.get_species(api_key, i, locale))

    for j in codes:
        for l in codes[codes.index(j):]:
            if j != l:
                if j['auteur'] == l['auteur']:
                    j['speciesList'] = list(set(j['speciesList']+l['speciesList']))
                    codes.pop(codes.index(l))
    SOTD=eb.speciesOTD(codes)
    speciesdict=eb.code_dict(api_key,SOTD, locale)

    out = ''
    for k in codes:
        out += k['auteur'] + ' have seen: '
        for l in k['speciesList']:
            out += speciesdict[l] + ', '
        out = out[:-2]+ '.\n \n'
    return out


if __name__ == '__main__':
    location = "SE" #Change your location here
    locale = "en"  #Put the language you want here.
    r = main(location, "")
    notifier = dn.Notifier('WEBHOOK URL') #Add your webhook url here.
    notifier.send('Yesterday, \n \n'+r, print_message=False)
