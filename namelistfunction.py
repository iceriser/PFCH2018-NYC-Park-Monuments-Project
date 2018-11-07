import csv

def build_name_list(art_data):

    #with open (art_data, 'r', encoding='utf-8') as f
    #reader = csv.reader(f)
    artist_list = []
    x = 0
    for row in art_data:
        while x < 10:
            if row[19] != '' and row[19] not in artist_list:
               artist_list.append(row[19])
               x = x + 1

    return artist_list
            
# While loop will later be removed once I'm confident I can resolve csv names with wikidata names.
