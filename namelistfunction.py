import csv
import re
import string

def build_name_list(art_data):

    #with open (art_data, 'r', encoding='utf-8') as f
    #reader = csv.reader(f)
    artist_list = []
    clean_names = []
    artist_list_clean = []
    #x = 0
    for row in art_data:
        #while x < 10:
        clean_names = re.compile('[;&/]').split(row[19])
        for name in clean_names:
            if name != '' and name not in artist_list and name != 'sculptor':
                artist_list.append(name)
    for name in artist_list:
        name = re.sub('(\(.*\))', '', name)
        name = string.capwords(name)
        if name not in artist_list_clean:
            artist_list_clean.append(name)
       
               
               #x = x + 1

    return artist_list_clean
            
# While loop will later be removed once I'm confident I can resolve csv names with wikidata names.

# Last resort is to use openrefine to clean data manually then use the cleaned data
