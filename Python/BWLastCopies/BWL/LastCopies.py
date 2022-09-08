from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import json
import urlsearch
import csv
datarows=[]
with open('.\Python\BWLastCopies\BWL\settings.json') as f:
    settings = json.load(f)
    csvfile=settings['csvfile']
#process each row of the xml file
#open the csv file with csv
with open(csvfile, newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    hasheader=csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)  # rewind
    if hasheader:
        next(reader)
    for row in reader:
        author=row['Verfasser']
        title=row['Titel']
        print(author,title)
'''for datarow in datarows:
    print(urlsearch.searchfromxml(datarow))
    '''