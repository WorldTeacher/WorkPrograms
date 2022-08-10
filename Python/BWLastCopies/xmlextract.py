import pandas as pd
from bs4 import BeautifulSoup
import time
import lxml
xml_file="./Python/BWLastCopies/test.xml"
with open(xml_file,encoding='utf-8') as f:
    data=f.readlines()

for line in data:
    #print(line)
    soup=BeautifulSoup(line,"lxml")
    #get the title
    title_data=soup.find("datafield",{"tag":"245"})
    soup1=BeautifulSoup(str(title_data),"lxml")
    title_field=soup1.find("subfield",{"code":"a"})
    soup1=BeautifulSoup(str(title_data),"lxml")
    title_field=soup1.find("subfield",{"code":"a"})
    title=title_field.text
    #print(title_field.text)
    #get the author
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
       #print(author_field.text)
    except:
        author="no author"
        #print(author)
    #get the issues
    try:
        issues_data=soup.find("datafield",{"tag":"250"})
        soup3=BeautifulSoup(str(issues_data),"lxml")
        issues_field=soup3.find("subfield",{"code":"a"})
        #print(issues_field)
        issues=issues_field.text
    except:
        issues="no issues"
        #print(issues)
    print('Title: '+title+' Author: '+author +' Issues: '+issues)
    '''if title_field is not None:
        title=title_field.text
    else:
        tags=["2","3","4","5","6"]
        for tag in tags:
            title_data=soup.find("datafield",{"tag":"245","ind1":"1","ind2":tag})
            soup1=BeautifulSoup(str(title_data),"lxml")
            title_field=soup1.find("subfield",{"code":"a"})
            title=title_field.text
            print(title_field)
            title=title_field.text
    #print(title_data)
    print(title_field.text)'''

    #except:
        #possible fields: tag="245" ind1="1" ind2="2,3,4,5,6" subfield="a"
        
            
        
    
    time.sleep(0.1)