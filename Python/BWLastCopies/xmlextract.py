import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import json
import logger
log=logger.log()
log.info_general('xmlextract.py started')
   
with open('settings.json') as config_file:
    config = json.load(config_file)
    log.info_general('config.json loaded')
def select():
    selector=input('select if the run should be a test or a full run (test/full/exit): ')
    try:
        if selector=='full':
            file=config['XML']
        
        elif selector=='test':
            file=config['XML-Test']
        elif selector=='exit':
            sys.exit()
        return file            
    except:
        print('wrong input, please try again')
        select()
def search(datafile):
    log.info_general('search started')
    print('search started, please wait')

    with open(datafile,encoding='utf-8') as f:
        data=f.readlines()
        length=len(data)
        print(f'length: {length}')
    xmldata=[]
    for line in data:
        x_data={'title':[],'author':[],'issue':[],'DE-640':[],'signature':[]}
        soup=BeautifulSoup(line,"lxml")
        
        x_data['title']=title_search(soup)
        x_data['author']=author_search(soup)
        x_data['issue']=issue_search(soup)
        x_data['signature']=signature_search(soup)
        xmldata.append(x_data)
        #request.get_xml(x_data['author'], x_data['title'])
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
    if title_field is not None:
        title=title_field.text
    else:
        title="0"
    #x_data['title']=title
    return title    
def author_search(soup):
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
        #print('100:'+author)
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
def signature_search(soup):
    try:
        signature_data=soup.find("datafield",{"tag":"852"})
        soup4=BeautifulSoup(str(signature_data),"lxml")
        signature_field=soup4.find("subfield",{"code":"c"})
        signature=signature_field.text
    except:
        signature="0"
    return signature
def make_csv(xmldata):
    df=pd.DataFrame(xmldata)
    #create csv at current directory
    df.to_csv(os.path.join(os.getcwd(),'BWL.csv'),index=False,sep='|')

def get_request():
    with open('BWL1.csv',encoding='utf-8') as f:
        data=f.readlines()
    xmldata=[]
    for line in data:
        linearray=line.split('|')
        print(f'line_title {linearray[0]}, line_author {linearray[1]}')
        #request.get_xml(line)
    
#time.sleep(0.1)

if __name__=="__main__":
    search(select())
    #get_request()
    print("done")
