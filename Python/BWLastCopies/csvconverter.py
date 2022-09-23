import csv
import json 
import pandas as pd
import time

with open('.\Python\BWLastCopies\BWL\settings.json') as f:
    settings = json.load(f)
    csvfile=settings['csvfile']
with open(csvfile,encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
    	#split the row into columns
        columns = row[0].split('|')
        print(columns)        
        time.sleep(5)

#df.to_json(r'./Python/BWLastCopies/BWL/jsonfile.json', orient='records')
