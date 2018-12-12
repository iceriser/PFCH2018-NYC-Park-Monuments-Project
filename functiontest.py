import csv
from namelistfunction import build_name_list
from wikidatafunction import grab_wikidata
from csvdatafunction import grab_csv_data

with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    results = build_name_list(reader)

    #print(*results, sep = '\n')

#datagrab = grab_wikidata('Frederick MacMonnies')
#if not datagrab:
    #datagrab.append('n/a')
    #datagrab.append('n/a')
    #datagrab.append('n/a')
    #datagrab.append('n/a')
    #datagrab.append('n/a')

#print(datagrab)

test_data = []    

for name in results:
    csvdata = grab_csv_data(name)
    test_data.append(csvdata)

print(test_data)    


