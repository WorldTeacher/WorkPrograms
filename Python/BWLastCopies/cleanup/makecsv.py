
import os #for paths
import glob
from turtle import title #searches files in paths
import pandas as pd #for csv open and read
import xml.etree.ElementTree as ET #for the url response
import time #for the delay
from urllib.request import urlopen #used to open the url 
import variables #list of all variables
import parts #smal codebits to make code cleaner
import re
import csv
titles=variables.titel_path
verfasser=variables.verfasser_path
#alldict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}
testdict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}
testdictlist=[]
titlelist=[]
cleantitlelist=[]
alist=[]
cleanverfasserlist=[]
urldict={'author':[],'title':[]}
alldictlist=[]
alllinks=[]
datafield_nodes_path = "./zs:records/zs:record/zs:recordData/record/datafield" 
ourlinks=[]
nmsp=variables.namespaces
subfield_sigil="DE-Frei129"
a=titles
b=verfasser


with open(a,"r") as file:
    lines=file.readlines()

for line in lines: #replace all symbols that might cause problems with the search
    #if !.: is in line, remove it
    line=line.replace("!","")
    line=line.replace(".","")
        
    line=line.replace(" ","%20")
    line=line.replace("\n","")
    line=line.replace("�","?")
    line=line.replace("?Der?","Der")
    line=line.replace("?Die?","Die")
    line=line.replace("?Das?","Das")
    line=line.replace("?The?","The")
    cleantitlelist.append(line)

with open(b,"r") as file:
    verflines=file.readlines()
for line in verflines:
    line=line.replace(" ","%20")
    line=line.replace("\n","")
    line=line.replace("�","?")
    line=line.replace(".","")
    cleanverfasserlist.append(line)


#add the two lists to a dictionary
#this only works under the assumption that the lists are the same length
for i in range(len(cleantitlelist)):
    urldict['title'].append(cleantitlelist[i])
    urldict['author'].append(cleanverfasserlist[i])
baseurl="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
base2url="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D20735&maximumRecords=10&recordSchema=marcxml"
for i in range(len(urldict['title'])):
    url=baseurl.replace("{title}",urldict['title'][i])
    url=url.replace("{author}",urldict['author'][i])
    alllinks.append(url)
for i in range(len(urldict['title'])):
    url2=base2url.replace("{title}",urldict['title'][i])
    url2=url2.replace("{author}",urldict['author'][i])
    ourlinks.append(url2)

total_issuelist=[]
title=[]
for i in range(len(alllinks)):
    alldict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}    
    #print(alllinks[i])
    #print(ourlinks[i])
    with urlopen(alllinks[i]) as response:
        xml = ET.parse(response)
        root = xml.getroot()
    datafield_attribute_filters=[#issue_filter,
        { 
            "tag":"250",
            "ind1":" ",
            "ind2":" ",
    }
    ]
    #search for the datafield attribute filter
   
    for datafield_node in root.iterfind(datafield_nodes_path, namespaces=nmsp):
        if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
            continue      
        for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
            #remove duplicate entries if they exist
            if subfield_node.text not in total_issuelist:
                #total_issuelist.append(subfield_node.text)
                alldict["total_issuelist"].append(subfield_node.text)
    datafield_attribute_filters=[#title
        { 
            "tag":"245",
            "ind1":"1",
            "ind2":"0",
    }
    ]
    title_count=0
    for datafield_node in root.iterfind(datafield_nodes_path, namespaces=nmsp):
        if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
            continue      
        for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
            if title_count==0:
                title.append(subfield_node.text)
                alldict["title"].append(subfield_node.text)
                title_count=title_count+1
    print(len(alldict["total_issuelist"]))
    if len(alldict["total_issuelist"])==0:
        alldict["total_issuelist"].append("ohne neuausgabe")
    datafield_attribute_filters=[{
                "tag":"924",
                "ind1":"0",
                "ind2":" ",
            }]
    for datafield_node in root.iterfind(datafield_nodes_path, namespaces=nmsp):
        if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
            continue
        for subfield_node in datafield_node.iterfind("./subfield[@code='b']", namespaces=nmsp):
            bib_count=len(subfield_node.text)
    with urlopen(ourlinks[i]) as response:
        xml = ET.parse(response)
        root = xml.getroot()
    datafield_attribute_filters=[{
                "tag":"924",
                "ind1":"0",
                "ind2":" ",
            }]
    for datafield_node in root.iterfind(datafield_nodes_path, namespaces=nmsp):
        if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
            continue
        for subfield_node in datafield_node.iterfind("./subfield[@code='b']", namespaces=nmsp):
            #bib_count=len(subfield_node.text)
            if subfield_node.text ==subfield_sigil:
                node=datafield_node.iterfind("./subfield[@code='g']", namespaces=nmsp)
                for subfield_node in node:
                    #signatur.append(subfield_node.text)
                    alldict["signatur"].append(subfield_node.text)
    alist.append(alldict)
    #reset alldict for new iteration

#make csv from alist

df=pd.DataFrame(alist)
df.to_csv("test7_2.csv",sep=";",index=False)  
for title in open(titles):
    #for each title, append it to testdict
    testdict['title'].append(title.strip())
    #add testdict to testdictlist
    testdictlist.append(testdict)
    #empty testdict for next title
    testdict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}

