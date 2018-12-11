import csv
from namelistfunction import build_name_list
from wikidatafunction import grab_wikidata
from csvdatafunction import grab_csv_data
import json

with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    name_list = build_name_list(reader)

all_data = []

i = 0

for name in name_list:
    datagrab = grab_wikidata(name)
    csvgrab = grab_csv_data(name)
    name_data = [name]
    name_data.append(datagrab)
    name_data.append(csvgrab)
    all_data.append(name_data)
    print(i)
    i=i+1

with open('monumentdata.json', 'w') as outfile:
    json.dump(all_data, outfile)

