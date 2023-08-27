import csv
#import pandas as pd

# ask for input for what to delete

with open('sane.csv', 'r', encoding='utf-8') as sane, open('sane1.csv', 'w+', encoding='utf-8') as sane1:
    reader1 = csv.reader(sane)
    reader2 = csv.reader(sane1)
    writer = csv.writer(sane1)

    for row in reader1:
        #print(row)
        if('harrison' not in row[1]):
           # writer.writerow(row)
            if ((('Harrison' not in row[3]) or ('harrison' not in row[3])) and ('Biblicality' not in row[3])):
                #if('"' in row[3] or 'â€' in row[3]):
                if('prof' not in row[3]) and ('curt' not in row[3]) and ('angus' not in row[3]):
                    #if('-' in row[3]):
                    writer.writerow(row)
                    print(row)

