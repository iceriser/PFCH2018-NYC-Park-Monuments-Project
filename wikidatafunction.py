import json
import requests
import wptools
import re
import Levenshtein
import time

def grab_wikidata(query):

    endpoint = "https://www.wikidata.org/w/api.php"

    params = { #remember to switch back to wbsearchentities if necessary
        'action' : 'query',
        'list' : 'search',
        'format' : 'json',
        #'language' : 'en',
        'srsearch' : query,
        'srwhat' : 'text',
        #'type' : 'item',
        'srlimit' : 10
        }

    r = requests.get(endpoint, params = params)

    rdict = json.loads(r.text)
    #print(rdict)

    queryvar = query
    #print(queryvar)

    i = 0

    name_data = {
        'birthdate' : 0,
        'birthplace' : 0,
        'death date' : 0,
        'death place' : 0
        }
        

    for name in rdict['query']['search']:

        #print(name['label'])
    
        #comparison = Levenshtein.distance(queryvar, name['label'])
        #print(comparison)
        #if comparison <= 2:
            #print('name match')

        page = wptools.page(wikibase=rdict['query']['search'][i]['title'])

        page.get_wikidata()

        datagrab = page.data['wikidata']
        #aliasinfo = page.data['aliases']
        #print(aliasinfo)
        #print(datagrab)
        try:
            if 'human (Q5)' in datagrab['instance of (P31)']:
                try:
                    aliasinfo = page.data['aliases']
                    print(aliasinfo)
                except:
                    print('no aliases')
                labelinfo = page.data['label']
                aliascheck = []
                comparison = Levenshtein.distance(queryvar, labelinfo)
                if comparison <= 3:
                    aliascheck.append('1')
                try:    
                    for aliases in aliasinfo:
                        comparison2 = Levenshtein.distance(queryvar, aliases)
                        if comparison2 <= 3:
                            aliascheck.append('1')
                        else:
                            aliascheck.append('0')
                except:
                    print('no aliases')
                    
                if '1' in aliascheck:            
                    if 'occupation (P106)' in datagrab and 'sculptor (Q1281618)' in datagrab['occupation (P106)']:
                        print('occupation match')
                        try:
                            name_data['birthdate'] = datagrab['date of birth (P569)']
                        except:
                            print('no birth date on record')
                            name_data['birthdate'] = 'n/a'
                        try:
                            name_data['birthplace'] = datagrab['place of birth (P19)']
                        except:
                            print('no birthplace on record')
                            name_data['birthplace'] = 'n/a'
                        try:
                            name_data['death date'] = datagrab['date of death (P570)']
                        except:
                            print('no death date on record')
                            name_data['death date'] = 'n/a'
                        try:
                            name_data['death place'] = datagrab['place of death (P20)']
                        except:
                            print('no place of death on record')
                            name_data['death place'] = 'n/a'
                    elif 'occupation (P106)' in datagrab and 'artist (Q483501)' in datagrab['occupation (P106)']:
                        print('occupation match')
                        try:
                            name_data['birthdate'] = datagrab['date of birth (P569)']
                        except:
                            print('no birth date on record')
                            name_data['birthdate'] = 'n/a'
                        try:
                            name_data['birthplace'] = datagrab['place of birth (P19)']
                        except:
                            print('no birthplace on record')
                            name_data['birthplace'] = 'n/a'
                        try:
                            name_data['death date'] = datagrab['date of death (P570)']
                        except:
                            print('no death date on record')
                            name_data['death date'] = 'n/a'
                        try:
                            name_data['death place'] = datagrab['place of death (P20)']
                        except:
                            print('no place of death on record')
                            name_data['death place'] = 'n/a'
                    else:
                        print('not an artist')
                else:
                    print('no matching names')
            else:
                print('not a person')
        except:
            print('insufficient data')
        i=i+1
    #print(name_data)
    if name_data['birthdate'] == 0:
        name_data['birthdate'] = 'n/a'
    if name_data['birthplace'] == 0:
        name_data['birthplace'] = 'n/a'
    if name_data['death date'] == 0:
        name_data['death date'] = 'n/a'
    if name_data['death place'] == 0:
        name_data['death place'] = 'n/a'    
    return name_data

   


#this searches for the query and displays the wikidata for the first 50 results
#next step is to set up a loop where the query is the name list items
#instead of displaying the data, instead saves the information for wikidata items with the career: sculptor (or artist)
#this data can then be combined with appropriate information from the csv
#before you push this to github ensure that you actually want to use query instead of wbsearchentities
#current issues: querying wikidata for a name with a typo produces no search results, if necessary could be remedied manually wbsearchentities uses the suggested search box, not the search page, using query might fix this
#using query allows access to the search page rather than the recommended items, may allow you to skip levenshtein distance entirely, base resolution entirely off of occupation matching. test tomorrow

#when the name is resolved, it produces false negatives in the occupation (RESOLVED: i'm a tool and misspelled occupation)
