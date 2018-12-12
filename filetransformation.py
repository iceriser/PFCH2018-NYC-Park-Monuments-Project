import csv
import json
import re

merged_data = {
    'artist' : '',
    'birthdate' : '',
    'birthplace' : '',
    'death date' : '',
    'death place' : '',
    'monument' : '',
    'borough' : [],
    'parkname' : [],
    'materials' : [],
    'cost' : [],
    }

merged_list = []

with open ('monumentdata.json') as json_data, open ('monumentdatafix.json', 'w') as fixed_file:
    d = json.load(json_data)
    for row in d:
        #print (row[1]['birthdate'])
        merged_data['artist'] = row[0]
        merged_data['birthdate'] = row[1]['birthdate']
        merged_data['birthdate'] = str(merged_data['birthdate'])
        merged_data['birthdate'] = re.sub('(-.*)', '', merged_data['birthdate'])
        merged_data['birthplace'] = row[1]['birthplace']
        merged_data['death date'] = row[1]['death date']
        merged_data['death place'] = row[1]['death place']
        merged_data['monument'] = row[2]['monument_name']
        merged_data['borough'] = row[2]['borough']
        merged_data['parkname'] = row[2]['parkname']
        merged_data['materials'] = row[2]['materials']
        merged_data['cost'] = row[2]['cost']
        #print(merged_data)
        merged_list.append(merged_data.copy())
         
    json.dump(merged_list, fixed_file)

#with open ('monumentdata.csv', 'w') as csv_file:
    


        
        
