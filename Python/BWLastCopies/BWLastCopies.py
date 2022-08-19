import os #for paths
import glob #searches files in paths
import pandas as pd #for csv open and read
import xml.etree.ElementTree as ET #for the url response
import time #for the delay
from urllib.request import urlopen #used to open the url 
import variables #list of all variables
import parts #smal codebits to make code cleaner
import re
import csv

#Define Variables needed for BWLastCopies Search
class BWLastCopies:
    def __init__(self):
        self.info=input('Print URLs? (y/n): ')
        self.namespaces=variables.namespaces
        self.datafield_nodes_path = "./zs:records/zs:record/zs:recordData/record/datafield"  # XPath
        self.subfield_sigil="DE-Frei129" #code="b"
        self.titel="C:/Users/aky547/GitHub/WorkPrograms/titel.txt"
        self.verfasser="C:/Users/aky547/GitHub/WorkPrograms/verfasser.txt"
        self.cleanverfasserlist=[]
        self.cleantitlelist=[]
        self.ourlinks=[]
        self.alllinks=[]
        self.urldict={'author':[],'title':[]}
        self.alldict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[]}
        self.dictlist=[]
        self.ourdictlist=[]
        self.ourdict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[]}
    
    def cleanup(self):
        a=self.titel
        b=self.verfasser
        
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
            self.cleantitlelist.append(line)

        with open(b,"r") as file:
            verflines=file.readlines()
        for line in verflines:
            line=line.replace(" ","%20")
            line=line.replace("\n","")
            line=line.replace("�","?")
            self.cleanverfasserlist.append(line)
        
        #add the two lists to a dictionary
        #this only works under the assumption that the lists are the same length
        for i in range(len(self.cleantitlelist)):
            self.urldict['title'].append(self.cleantitlelist[i])
            self.urldict['author'].append(self.cleanverfasserlist[i])
        
    
    def URLGenerator(self):
        baseurl="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
        base2url="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D20735&maximumRecords=10&recordSchema=marcxml"
        for i in range(len(self.urldict['title'])):
            url=baseurl.replace("{title}",self.urldict['title'][i])
            url=url.replace("{author}",self.urldict['author'][i])
            self.alllinks.append(url)
        for i in range(len(self.urldict['title'])):
            url2=base2url.replace("{title}",self.urldict['title'][i])
            url2=url2.replace("{author}",self.urldict['author'][i])
            self.ourlinks.append(url2)
        print('oururl:',self.ourlinks)

#for files in testfile:

    def Search(self):
        
        lis=['title','number of titles','own_issuelist','signatur','owncount','total_issuelist']
        #w"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DJava%20ist%20auch%20eine%20Insel&maximumRecords=10&recordSchema=marcxml") as file:
        #title=[]
        #issuelist_own=[]
        #total_issuelist=[]
        #signatur=[]
        nmsp=self.namespaces
        for row in self.alllinks:
            if self.info == 'y':
                print(row)
            else:pass
            
            title=[]
            
            total_issuelist=[]
            signatur=[]
            owncount=0
            totalcount=0
            with urlopen(row) as file:
                    #print(file)
                    doc=ET.parse(file)
                    root=doc.getroot()
                    #file.close()
            #the code below gets the data for all available issues in the xml 
            datafield_attribute_filters=[#issue_filter,
                { #testing needed
                    "tag":"250",
                    "ind1":" ",
                    "ind2":" ",
            }
            ]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue      
                newroot=ET.fromstring(ET.tostring(datafield_node))
                for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=self.namespaces):
                    #remove duplicate entries if they exist
                    if subfield_node.text not in total_issuelist:
                        total_issuelist.append(subfield_node.text)
        
                    
                    #total_issuelist.append(subfield_node.text)      
                                        
            #the code below gets the data for the title in the xml           
            datafield_attribute_filters = [
            {
            "tag": "245", #title
            "ind1": "1",
            "ind2": "0",
            }] 
            title_append=0
        
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                if title_append==0:
                    for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
                        title.append(subfield_node.text)
                        #alldict['title'].append(subfield_node.text)
                        #searchtitle=subfield_node.text
                        
                        titlecount=len(subfield_node.text)
                        #alldict["number of titles"].append(titlecount)
                        title_append+=1
        
            #the code below gets the data for the signatur in the xml
        
            datafield_attribute_filters=[{
                "tag":"924",
                "ind1":"0",
                "ind2":" ",
            }]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                for subfield_node in datafield_node.iterfind("./subfield[@code='b']", namespaces=nmsp):
                    
                    if subfield_node.text ==self.subfield_sigil:
                        node=datafield_node.iterfind("./subfield[@code='g']", namespaces=nmsp)
                        for subfield_node in node:
                            signatur.append(subfield_node.text)
                            #alldict['signatur'].append(subfield_node.text)
            self.alldict['title']=title
            self.alldict['number of titles']=titlecount
            #self.alldict['own_issuelist']=issuelist_own
            self.alldict['signatur']=signatur
            #self.alldict['owncount']=len(issuelist_own)
            self.alldict['total_issuelist']=total_issuelist
            
            
            self.dictlist.append(self.alldict.copy())
            #print(dictlist)
            self.alldict.clear()
        
        #dictlist to csv usnig pandas
        #print(dictlist)
        #df=pd.DataFrame(dictlist)
        #df.to_csv('test.csv',sep=';',index=False)
        
        #print(dictlist)
        
            #the code below makes a new search and finds out issue and the count of the books
            #url="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D"+ searchtitle + "+and+pica.bib=20735&maximumRecords=10&recordSchema=marcxml"
    def OurSearch(self):
        
        lis=['title','number of titles','own_issuelist','signatur','owncount','total_issuelist']
        #w"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DJava%20ist%20auch%20eine%20Insel&maximumRecords=10&recordSchema=marcxml") as file:
        #title=[]
        #issuelist_own=[]
        #total_issuelist=[]
        #signatur=[]
        nmsp=self.namespaces
        for row in self.alllinks:
            if self.info == 'c':
                print(row)
            else:pass
            
            title=[]
            
            own_issuelist=[]
            oursignatur=[]
            owncount=0
            #totalcount=0
            with urlopen(row) as file:
                    #print(file)
                    doc=ET.parse(file)
                    root=doc.getroot()
                    #file.close()
            #the code below gets the data for all available issues in the xml 
            datafield_attribute_filters=[#issue_filter,
                { #testing needed
                    "tag":"250",
                    "ind1":" ",
                    "ind2":" ",
            }
            ]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue      
                newroot=ET.fromstring(ET.tostring(datafield_node))
                for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=self.namespaces):
                    #remove duplicate entries if they exist
                    if subfield_node.text not in own_issuelist:
                        own_issuelist.append(subfield_node.text)
        
                    
                    #total_issuelist.append(subfield_node.text)      
                                        
            #the code below gets the data for the title in the xml           
            datafield_attribute_filters = [
            {
            "tag": "245", #title
            "ind1": "1",
            "ind2": "0",
            }] 
            title_append=0
        
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                if title_append==0:
                    for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
                        title.append(subfield_node.text)
                        #alldict['title'].append(subfield_node.text)
                        #searchtitle=subfield_node.text
                        
                        titlecount=len(subfield_node.text)
                        #alldict["number of titles"].append(titlecount)
                        title_append+=1
        
            #the code below gets the data for the signatur in the xml
        
            datafield_attribute_filters=[{
                "tag":"924",
                "ind1":"0",
                "ind2":" ",
            }]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                for subfield_node in datafield_node.iterfind("./subfield[@code='b']", namespaces=nmsp):
                    
                    if subfield_node.text ==self.subfield_sigil:
                        node=datafield_node.iterfind("./subfield[@code='g']", namespaces=nmsp)
                        for subfield_node in node:
                            oursignatur.append(subfield_node.text)
                            #alldict['signatur'].append(subfield_node.text)
            self.ourdict['title']=title
            self.ourdict['number of titles']=titlecount
            #self.alldict['own_issuelist']=issuelist_own
            self.ourdict['signatur']=oursignatur
            #self.alldict['owncount']=len(issuelist_own)
            self.ourdict['total_issuelist']=own_issuelist
            
            print(self.ourdict)
            self.ourdictlist.append(self.ourdict.copy())
            #print(dictlist)
            self.ourdict.clear()
        
    def ourSearch1(self):
        issuelist_own=[]
        ourtitle=[]
        nmsp=self.namespaces
        for url in self.ourlinks:
            if self.info == 'y':
                print(url)
            else:pass  
            with urlopen(url) as ownsearch:
                doc=ET.parse(ownsearch)
                root=doc.getroot()
                ownsearch.close()
            datafield_attribute_filters=[{
                "tag":"924",
                "ind1":"0",
                "ind2":" ",
            }]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                #rootofown=datafield_node.find("./]", namespaces=namespaces)
                if any(datafield_node.get(k) != v for attr_dict in variables.issue_filter for k,v in attr_dict.items()):
                    continue
                for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
                    issuelist_own.append(subfield_node.text)
                    owncount=len(issuelist_own)
            #the code below gets the data for the title in the xml           
            datafield_attribute_filters = [
            {
            "tag": "245", #title
            "ind1": "1",
            "ind2": "0",
            }] 
            title_append=0
        
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                if title_append==0:
                    for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=nmsp):
                        ourtitle.append(subfield_node.text)
                        #alldict['title'].append(subfield_node.text)
                        #searchtitle=subfield_node.text
                        
                        titlecount=len(subfield_node.text)
                        #alldict["number of titles"].append(titlecount)
                        title_append+=1
            datafield_attribute_filters=[#issue_filter,
                { #testing needed
                    "tag":"250",
                    "ind1":" ",
                    "ind2":" ",
            }
            ]
            for datafield_node in root.iterfind(self.datafield_nodes_path, namespaces=nmsp):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue      
                for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=self.namespaces):
                    #remove duplicate entries if they exist
                    if subfield_node.text not in issuelist_own:
                        issuelist_own.append(subfield_node.text)
                        owncount=len(issuelist_own)
            self.ourdict['title']=ourtitle
            self.ourdict['issuelist_own']=issuelist_own
            self.ourdict['owncount']=owncount
            self.ourdictlist.append(self.ourdict.copy())
            print(self.ourdictlist)
            self.ourdict.clear()
            #print(title_append)
    def make_csv(self):
        #print('all: ',self.dictlist)
        print('our: ',self.ourdictlist)     
        '''#merge the two lists
        mergelist=self.dictlist+self.ourdictlist
        print('merged: ',mergelist)
        #make a csv file
        df=pd.DataFrame(mergelist)
        df.to_csv('testmerged.csv',sep=';',index=False)'''   
if __name__ == '__main__':
    bwl=BWLastCopies()
    bwl.cleanup()
    bwl.URLGenerator()
    #bwl.Search()
    bwl.OurSearch()
    #bwl.make_csv()