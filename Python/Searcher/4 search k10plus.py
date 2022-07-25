import os #for paths
import glob #searches files in paths
import pandas as pd #for csv open and read
import xml.etree.ElementTree as ET #for the url response
import time #for the delay
from urllib.request import urlopen #used to open the url 
import variables #list of all variables
import parts #smal codebits to make code cleaner
import re




def K10Plus(query):
    url_template = "https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{author}+and+pica.per%3D{title}+and+pica.bib%3D20735&maximumRecords=10&recordSchema=marcxml"
    
    print(query)
    for file in query:
        urllist=[]
       # print('working on ' + file)
        csv=pd.read_csv(file, sep='\t', encoding='utf-8')
        #print(csv)
        param1={'author':[], 'title':[]}
        
        #append the author and title to the param1 dictionary
        authlist=[]
        titlist=[]
        a=[[1,2,3,4],[5,6,7,8]]
        '''for row in csv['Author']:
            authlist.append(row)
        
        for row in csv['Title']:
            row=re.sub(r'\x98', '', str(row) ) #regex to remove the \x98
            row=re.sub(r'\x9c', '', str(row) ) #regex to remove the \x9c
            titlist.append(row)'''
        for row in csv.iterrows():
            print(row[1]['Author'])
        #merge the lists
        #print(authlist)
        #print(titlist)
        #twodlist=[authlist, titlist]
        #print(twodlist)
        #for row in twodlist:
        #    print(row)
        #    for item in row:
        #        print('item',item)
                #for i in item:
                #    print(i)
        '''for row in csv['Author']:
            autor=row
            for row in csv['Title']:
            titel=re.sub(r'\x98', '', str(row) ) #regex to remove the \x98
            titel=re.sub('\x9c', '', str(row) ) #regex to remove the \x9c
            url=url_template.format(author=autor,title=titel)
            #urllist.append(url)
        for row in csv['Title']:
            row=re.sub(r'\x98', '', str(row) ) #regex to remove the \x98
            row=re.sub('\x9c', '', str(row) ) #regex to remove the \x9c   
            url=url_template.format(title=row)
            urllist.append(url)
            param1['title'].append(row)
        print(urllist)
        
        '''
        #make url
        #print(param1['author'] + param1['title'])
        '''for author, title in param1['author']:
            print(author)
            for entry in title:
                print('Author: ' + str(entry))
                time.sleep(0.25)
            #for string in title:
            #    print('Title: ' + string)
            #url = url_template.format(param1['author'], param1['title'])
            #urllist.append(url)
        #print(urllist)'''
            
    
        
if __name__=='__main__':
    K10Plus(query=variables.test)
