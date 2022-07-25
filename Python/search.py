import os #for paths
import glob

import pandas as pd #for csv open and read
import xml.etree.ElementTree as ET #for the url response
import time #for the delay
from urllib.request import urlopen #used to open the url 
import Python.Searcher.variables as variables #list of all variables
import parts #smal codebits to make code cleaner
import re



def K10Plus(query):
    url_template = "https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.per%3D{author}+and+pica.bib%3D20735&maximumRecords=10&recordSchema=marcxml"
    file_list=[]
    for file in query:
            
        urllist=[]
        paramlist=[]
        
        csv=pd.read_csv(file,  sep='\t', encoding='utf-8')

        
        param={'author':[],'title':[]}
        #print(csv)
        
        for row in csv.iterrows():
            param['author']=row[1]['Clean_Author']
           
            
            
            param['title']=row[1]['Clean_Title']
            #print(param['title'])
            paramlist.append(param)
            #print(row[1]['line'])
        #make url
            url=url_template.format(title=param['title'], author=param['author'])
            
            urllist.append(url)
            '''with urlopen(url) as response:
                doc = ET.parse(response)  
                root = doc.getroot()
'''
        print(urllist)
if __name__=='__main__':
    K10Plus(query=variables.filelist_4)
