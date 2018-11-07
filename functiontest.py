import csv
from namelistfunction import build_name_list

with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    results = build_name_list(reader)

    print(results)

#This currently produces nothing, ask about it in class.
