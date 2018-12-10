import csv
from namelistfunction import build_name_list
from wikidatafunction import grab_wikidata

#with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    #reader = csv.reader(f)
    #results = build_name_list(reader)

    #print(*results, sep = '\n')

datagrab = grab_wikidata('Philip Martiny')

print(datagrab)


