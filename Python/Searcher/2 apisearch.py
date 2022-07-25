import glob
import pandas as pd
from urllib.request import urlopen
import os
import variables
import variables
import parts
#this generates a new csv for each cleaned csv in the extract/isbnlist folder. This csv only contains the link to the api search. 

#if not os.path.exists(safepath_2):
 #   os.makedirs(safepath_2)

for file in variables.filelist_2:
    print(file)
    #read csv, make a list of all isbns
    data=pd.read_csv(file, sep="\t",  encoding='utf8')
    list=[]
    for row in data['ISBN']:
        list.append(row)
    apisearch=[]  
    for isbn in list: #this generates the isbnlist for the api search
        url = 'http://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=ISBN%3D' + str(isbn) + '&recordSchema=MARC21-xml'
        apisearch.append(url) #changed http://sru.k10plus.de/gvk! to http://sru.k10plus.de/opac-de-627! since this should report all titles we own, gvk seems to be filtered (acc. to source)
    
    urllinks=pd.DataFrame({'URL' : apisearch})
    urllinks.to_csv(str(variables.isbnlist) + os.path.basename(file) +"-urllist.csv", sep='\t', encoding='utf8')
    parts.rename(variables.isbnlist)
    parts.delete_files(file)

'''#delete the old csv files
parts.delete_files(extractReiheA)
'''