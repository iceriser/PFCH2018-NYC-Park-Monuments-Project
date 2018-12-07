import json
import requests
import wptools
import re
import Levenshtein

def grab_wikidata(query):

    endpoint = "https://www.wikidata.org/w/api.php"

    params = {
        'action' : 'wbsearchentities',
        'format' : 'json',
        'language' : 'en',
        'search' : query,
        'type' : 'item',
        'limit' : 50
        }

    r = requests.get(endpoint, params = params)

    rdict = json.loads(r.text)

    queryvar = query
    print(queryvar)

    i = 0

    name_data = []

    for name in rdict['search']:

        print(name['label'])
    
        comparison = Levenshtein.distance(queryvar, name['label'])
        print(comparison)
        if comparison <= 2:
            print('name match')

            page = wptools.page(wikibase=rdict['search'][i]['title'])

            page.get_wikidata()

            datagrab = page.data['wikidata']
            print(datagrab)
            if 'occupation (P106)' in datagrab and 'sculptor (Q1281618)' in datagrab['occupation (P106)']:
                print('occupation match')
                name_data.append(datagrab)
            elif 'occupation (P106)' in datagrab and 'artist (Q483501)' in datagrab['occupation (P106)']:
                print('occupation match')
                name_data.append(datagrab)
            else:
                print('not an artist')
        i=i+1
    return name_data

   


#this searches for the query and displays the wikidata for the first 50 results
#next step is to set up a loop where the query is the name list items
#instead of displaying the data, instead saves the information for wikidata items with the career: sculptor (or artist)
#this data can then be combined with appropriate information from the csv

#current issues: querying wikidata for a name with a typo produces no search results, if necessary could be remedied manually wbsearchentities uses the suggested search box, not the search page, using query might fix this
#when the name is resolved, it produces false negatives in the occupation (RESOLVED: i'm a tool and misspelled occupation)
