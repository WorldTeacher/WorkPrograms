import os
import glob
import time
import datetime as dt
from urllib.request import urlopen
import pandas as pd
import xml.etree.ElementTree as ET
import parts
import variables
import re

def DNBQuery(query):
    for file in query:
        starttime= time.time()
        csvfile = pd.read_csv(file, sep='\t', encoding='utf-8')
        clean_aut = []
        title = []
        for row in csvfile['URL']:
            #if row has %3D-& skip 
            if '%3D-&' in row: #for error in url, courtesy of dnbs crappy database
                clean_aut.append(None)
                title.append(None)
                continue
            with urlopen(str(row)) as response:
                doc = ET.parse(response)  
                root = doc.getroot()
                namespaces = {  # Manually extracted from the XML file, but there could be code written to automatically do that.
            "zs": "http://www.loc.gov/zing/srw/",
            "": "http://www.loc.gov/MARC21/slim",
                }
            datafield_nodes_path = "./zs:records/zs:record/zs:recordData/record/datafield"  # XPath
            datafield_attribute_filters = [ #which fields to extract
            {
            "tag": "100", #author
            "ind1": "1",
            "ind2": " ",
            }]     
            auth_append= 0
            no_aut = True
            for datafield_node in root.iterfind(datafield_nodes_path, namespaces=namespaces):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue      
                if auth_append==0:
                    for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=namespaces):
                        for char in subfield_node.text:
                            if char is '.':
                                
                        clean_aut.append(subfield_node.text) #this gets the author name
                        no_aut = False
                        auth_append+=1
            if no_aut: clean_aut.append(None)
            datafield_attribute_filters = [
            {
            "tag": "245", #title
            "ind1": "1",
            "ind2": "0",
            }] 
            title_append=0
            no_title = True
            for datafield_node in root.iterfind(datafield_nodes_path, namespaces=namespaces):
                if any(datafield_node.get(k) != v for attr_dict in datafield_attribute_filters for k,v in attr_dict.items()):
                    continue
                if title_append==0:
                    for subfield_node in datafield_node.iterfind("./subfield[@code='a']", namespaces=namespaces):
                        title_append+=1
                        subfield_node.text=re.sub(r'\x98', '', subfield_node.text) #regex to remove the \x98
                        subfield_node.text=re.sub(r'\x9c', '', subfield_node.text)
                        title.append(subfield_node.text)
                        no_title = False      
            if no_title: title.append(None)
        
        print(row)
        origdata=pd.DataFrame({"Clean_Author":clean_aut, "Clean_Title":title})	
        #origdata=pd.DataFrame({'Author':clean_aut, 'Title':title})                      
        origdata.to_csv(str(variables.dnbresult) + os.path.basename(file)  +"-additdata.csv", sep='\t', encoding='utf8')
        #os.remove(file) 
        #print(clean_aut)
        print(origdata)
        endtime=time.time()
        duration=endtime-starttime
        print("the file took",round(duration),"sec to complete")
        parts.rename(variables.dnbresult)
        parts.delete_files(file)
if __name__ == "__main__":
    DNBQuery(variables.filelist_3)



 

        
        
       