import json
import requests
import wptools
import re

endpoint = "https://www.wikidata.org/w/api.php"

query = "Tery Fugate-Wilcox"

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


i = 0
for name in rdict['search']:
    
    
    page = wptools.page(wikibase=rdict['search'][i]['title'])

    page.get_wikidata()

    print(page.data['wikidata'])

    i=i+1


#this searches for the query and displays the wikidata for the first 50 results
#next step is to set up a loop where the query is the name list items
#instead of displaying the data, instead saves the information for wikidata items with the career: sculptor (or artist)
#this data can then be combined with appropriate information from the csv    
