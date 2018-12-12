import re
import Levenshtein
import time
import csv

def grab_csv_data(list_name):

    csv_data = {
        'monument_name' : [],
        'borough' : [],
        'parkname' : [],
        'materials' : [],
        'cost' : []
        }
        

    with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if list_name.lower() in row[19].lower():
                if row[0] not in csv_data['monument_name']:
                    csv_data['monument_name'].append(row[0])
                if row[4] not in csv_data['borough']:
                    csv_data['borough'].append(row[4])
                if row[5] not in csv_data['parkname']:
                    csv_data['parkname'].append(row[5])
                if row[16] not in csv_data['materials']:
                    csv_data['materials'].append(row[16])
                if row[30] not in csv_data['cost']:    
                    csv_data['cost'].append(row[30])

    return csv_data            
