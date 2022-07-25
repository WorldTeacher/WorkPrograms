import glob
import os
import parts
import pandas as pd
import Python.Searcher.variables as variables

class WebScraper:
    def __init__(self) -> None:
        self.dnburl = 'http://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=ISBN%3D' + str(isbn) + '&recordSchema=MARC21-xml'
        self.list1=variables.filelist_1
        self.list2=variables.filelist_2
        self.extract=variables.extractReiheA
        pass
    def remove_unneeded_parts(self):
        for file in start:
            data=pd.read_csv(file, sep="\t",  encoding='utf8')
            data.columns
            #append Data based on rows
            title=[] #this gets all the titles
            for row in data['Titel']:
                title.append(row)
            author=[] #this gets all the authors
            for row in data['Verfasser']:
                author.append(row)
            isbn=[] #this gets all the isbns
            for row in data['ISBN']:
                isbn.append(row)
            df=pd.DataFrame({'Verfasser': author, 'Titel': title, 'ISBN': isbn}) #create new csvs based on extracted data
            #discrading unneeded parts 
            df['ISBN'] = [x.split('; ')[0] for x in data['ISBN']] #discards the second isbn.
            df['Verfasser'] = [x.split('; ')[0] for x in data['Verfasser']] #discards everything after the first author.
            #save csv in set path
            df.to_csv(str(self.extract) + os.path.basename(file) + '-extract.csv', sep='\t', encoding='utf8')
            print(file +' saved to ' + self.extract)
        parts.rename(self.extract)
    
    def urlgen(self):
        for file in self.list2:
            print(file)
            #read csv, make a list of all isbns
            data=pd.read_csv(file, sep="\t",  encoding='utf8')
            list=[]
            for row in data['ISBN']:
                list.append(row)
            apisearch=[]  
            for isbn in list: #this generates the isbnlist for the api search
                apisearch.append(self.dnburl) #changed http://sru.k10plus.de/gvk! to http://sru.k10plus.de/opac-de-627! since this should report all titles we own, gvk seems to be filtered (acc. to source)
            
            urllinks=pd.DataFrame({'URL' : apisearch})
            urllinks.to_csv(str(variables.isbnlist) + os.path.basename(file) +"-urllist.csv", sep='\t', encoding='utf8')
            parts.rename(variables.isbnlist)
            parts.delete_files(file)