import csv
from namelistfunction import build_name_list
from wikidatafunction import grab_wikidata

with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    name_list = build_name_list(reader)

all_data = []

for name in name_list:
    datagrab = grab_wikidata(name)
    name_data = [name]
    name_data.append(datagrab)
    all_data.append(name_data)

print(all_data)
