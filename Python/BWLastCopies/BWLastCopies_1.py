
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
import logger
import threading #for multithreading, work in progress
bib_id=20735
#Define Variables needed for BWLastCopies Search
class BWLastCopies:
    log=logger.log()
    def __init__(self):
        self.info=input('Print URLs? (y/n): ')
        self.log=input('Log URLs? (y/n): ')
        self.namespaces=variables.namespaces
        self.datafield_nodes_path = "./zs:records/zs:record/zs:recordData/record/datafield"  # XPath
        self.subfield_sigil="DE-Frei129" #code="b"
        self.titel=variables.titel_path
        self.verfasser=variables.verfasser_path
        self.cleanverfasserlist=[]
        self.cleantitlelist=[]
        self.oururls=[]
        self.allurls=[]
        self.urldict={'author':[],'title':[]}
        self.ourdict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}
        self.fieldname=['title','number of titles','own_issuelist','signatur','owncount','total_issuelist','bibcount']
        self.alldict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}
        self.alldictlist=[]
        self.ourdictlist=[]
        self.baseurl="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
        self.base2url="https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D"+str(bib_id)+"&maximumRecords=10&recordSchema=marcxml"
        
    
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
            line=line.replace("¬Ein¬","Ein")
            line=line.replace("¬Der¬","Der")
            line=line.replace("¬Die¬","Die")
            line=line.replace("¬Das¬","Das")

            self.cleantitlelist.append(line)

        with open(b,"r") as file:
            verflines=file.readlines()
        for line in verflines:
            line=line.replace(" ","%20")
            line=line.replace("\n","")
            line=line.replace("�","?")
            line=line.replace(".","")
            self.cleanverfasserlist.append(line)
        
        #add the two lists to a dictionary
        #this only works under the assumption that the lists are the same length
        for i in range(len(self.cleantitlelist)):
            self.urldict['title'].append(self.cleantitlelist[i])
            self.urldict['author'].append(self.cleanverfasserlist[i])
        
    
    def URLGenerator(self):
        for i in range(len(self.urldict['title'])):
            url=self.baseurl.replace("{title}",self.urldict['title'][i])
            url=url.replace("{author}",self.urldict['author'][i])
            self.allurls.append(url)
        for i in range(len(self.urldict['title'])):
            url2=self.base2url.replace("{title}",self.urldict['title'][i])
            url2=url2.replace("{author}",self.urldict['author'][i])
            self.oururls.append(url2)

    def totalSearch(self): #this is the attempt to search both urls and make a single list of the results
        title=[]
        titlecount=0
        number_of_titles=0
        own_issuelist=[]
        signatur=[]
        owncount=0
        total_issuelist=[]
        nmsp=self.namespaces
        for i in range(len(self.urldict['title'])):
            alldict={'title':[],'number of titles':[],'signatur':[],'owncount':[],'own_issuelist':[],'total_issuelist':[],'bibcount':[],'ppn':[]}

            print(i)
            if self.info == 'y':
                print('ALL: ',self.allurls[i])
            else:pass
            with urlopen(self.allurls[i]) as file:
                    #print(file)
                    doc=ET.parse(file)
                    root=doc.getroot()
                    
            datafield_attribute_filters=[#issue_filter,
                { 
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
                    if subfield_node.text not in total_issuelist:
                        alldict["total_issuelist"].append(subfield_node.text)
                                                
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
                        #title.append(subfield_node.text)                       
                        alldict["title"].append(subfield_node.text)
                        titlecount=len(subfield_node.text)
                        alldict["number of titles"].append(titlecount)
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
                    alldict["bibcount"]=len(subfield_node.text)
                    '''if subfield_node.text ==self.subfield_sigil:
                        node=datafield_node.iterfind("./subfield[@code='g']", namespaces=nmsp)
                        for subfield_node in node:
                            signatur.append(subfield_node.text)'''
        
            if self.info == 'y':
                print('Our: ',self.oururls[i])
            else:pass
            with urlopen(self.oururls[i]) as file:
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
                        #own_issuelist.append(subfield_node.text)
                        alldict["own_issuelist"].append(subfield_node.text)
                    
                    #total_issuelist.append(subfield_node.text)      
                                        
            #the code below gets the data for the title in the xml           
            '''datafield_attribute_filters = [
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
                        title_append+=1'''
        
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
                    #bib_count=len(subfield_node.text)
                    if subfield_node.text ==self.subfield_sigil:
                        node=datafield_node.iterfind("./subfield[@code='g']", namespaces=nmsp)
                        for subfield_node in node:
                            #signatur.append(subfield_node.text)
                            alldict["signatur"].append(subfield_node.text)

            #alldict['title'].append(title)
            #alldict['number of titles'].append(titlecount)
            #alldict['own_issuelist'].append(own_issuelist)
            #alldict['signatur'].append(signatur)
            alldict['owncount']=len(own_issuelist)
            #alldict['total_issuelist'].append(total_issuelist)
            #alldict['bib_count']=bib_count
            
            print(alldict)
            self.alldictlist.append(alldict)
        #empty alldict for the next iteration
        #alldict={'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]}


        #self.alldict.clear()

            
            
    def make_csv(self):
        #print(self.ourdict)
        print(self.alldictlist)
        df=pd.DataFrame.from_dict(self.alldictlist)
        df.to_csv('test8_sort.csv',sep=';', index=False)
                #print('all: ',self.alldictlist)
        #print('our: ',self.ourdictlist)  
        #make a csv out of alldictlist
        #df=pd.DataFrame(self.alldictlist)
        #df.to_csv('testaio.csv', sep=';',index=False)   
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
   
    bwl.totalSearch()
    bwl.make_csv()