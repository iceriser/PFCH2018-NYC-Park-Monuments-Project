import csv
import re
import string

with open ('NYC_Parks_Monuments.csv', 'r', encoding='utf-8') as f:
    art_data = csv.reader(f)

    artist_list = []
    artist_list_item = []
    clean_names = []
    artist_list_clean = []

    for row in art_data:
        #print(row)
        original_name = row[19]
        #print(original_name)
        clean_names = re.compile('[;&/]').split(row[19])
        #print(row[19])
        for name in clean_names:
            if name != '' and name not in artist_list_item and name != 'sculptor':
                artist_list_item.append(name)
                artist_list_item.append(original_name)
                artist_list.append(artist_list_item)
        for name in artist_list:
            for row in art_data:
                print(artist_list[name][1])
                if row[19] in artist_list[name][1]:
                    artist_list[name].append(row)
            print(name[0])        
            name[0] = re.sub('(\(.*\))', '', name[0])
            name[0] = string.capwords(name[0])
            print(name[0])
            if name[0] not in artist_list_clean:
                artist_list_clean.append(name)
               
                    
                
#with open('namelisttest.text', 'w') as f:
    #for name in artist_list:
            #f.writelines('%s\n' % name)


            

    

    
   
