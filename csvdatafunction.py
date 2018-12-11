import re
import Levenshtein
import time
import csv

def grab_csv_data(list_name):

    csv_data = []

    with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if list_name.lower() in row[19].lower():
                csv_data.append(row[4])
                csv_data.append(row[5])
                csv_data.append(row[9])
                csv_data.append(row[16])
                csv_data.append(row[30])

    return csv_data            
