import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import time
import lxml
import json
import logger
log=logger.log()
log.info_general('xmlextract.py started')
selector=input('select if the run should be a test or a full run (test/full): ')
if selector=='test':
    selector_fine=input('select if the run should be a short test or a long test (short/long): ')
    
with open('config.json') as config_file:
    config = json.load(config_file)
    log.info_general('config.json loaded')
file=config['XML']['Final']
print(file)
def search(datafile):
    log.info_general('search started')
    print('search started, please wait')

    with open(datafile,encoding='utf-8') as f:
        data=f.readlines()
    xmldata=[]
    for line in data:
        x_data={'title':[],'author':[],'issue':[],'DE-640':[]}
        soup=BeautifulSoup(line,"lxml")
        
        x_data['title']=title_search(soup)
        x_data['author']=author_search(soup)
        x_data['issue']=issue_search(soup)
        xmldata.append(x_data)
        ''' try:
            de640_data=soup.find("datafield",{"tag":"583"})
            soup4=BeautifulSoup(str(de640_data),"lxml")
            de640_field=soup4.find("subfield",{"code":"z"})
            de640=de640_field.text
            x_data['DE-640']=de640
        except:
            de640="no de640"
            x_data['DE-640']=de640'''
    make_csv(xmldata)    
def title_search(soup):
    title_data=soup.find("datafield",{"tag":"245"})
    soup1=BeautifulSoup(str(title_data),"lxml")
    title_field=soup1.find("subfield",{"code":"a"})
    soup1=BeautifulSoup(str(title_data),"lxml")
    title_field=soup1.find("subfield",{"code":"a"})
    title=title_field.text
    #x_data['title']=title
    return title    
def author_search(soup):
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
        print('100:'+author)
        #x_data['author']=author
    except:
        author_data=soup.find("datafield",{"tag":"700"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        if author_field is not None:
            author=author_field.text
        #print('700: '+author_field.text)
        else:
            author="0"
    return author
def issue_search(soup):
    try:
        issues_data=soup.find("datafield",{"tag":"250"})
        soup3=BeautifulSoup(str(issues_data),"lxml")
        issues_field=soup3.find("subfield",{"code":"a"})
        issues=issues_field.text
    except:
        issues="0"
    return issues
def make_csv(xmldata):
    df=pd.DataFrame(xmldata)
    #create csv at current directory
    df.to_csv(os.path.join(os.getcwd(),'BWL.csv'),index=False)


    
#time.sleep(0.1)

if __name__=="__main__":
    search(file)
    print("done")
