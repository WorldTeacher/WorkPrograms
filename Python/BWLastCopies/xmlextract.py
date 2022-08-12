from types import NoneType
import pandas as pd
from bs4 import BeautifulSoup
import time
import lxml
xml_file="./Python/BWLastCopies/test-short.xml"
def search():
    with open(xml_file,encoding='utf-8') as f:
        data=f.readlines()
    xmldata=[]
    for line in data:
        x_data={'title':[],'author':[],'issue':[],'DE-640':[]}
        soup=BeautifulSoup(line,"lxml")
        title_data=soup.find("datafield",{"tag":"245"})
        soup1=BeautifulSoup(str(title_data),"lxml")
        title_field=soup1.find("subfield",{"code":"a"})
        soup1=BeautifulSoup(str(title_data),"lxml")
        title_field=soup1.find("subfield",{"code":"a"})
        title=title_field.text
        x_data['title']=title
        author_search(soup)
            
        time.sleep(1)
        try:
            issues_data=soup.find("datafield",{"tag":"250"})
            soup3=BeautifulSoup(str(issues_data),"lxml")
            issues_field=soup3.find("subfield",{"code":"a"})
            issues=issues_field.text
            x_data['issue']=issues
        except:
            issues="no issues"
            x_data['issue']=issues
        try:
            de640_data=soup.find("datafield",{"tag":"583"})
            soup4=BeautifulSoup(str(de640_data),"lxml")
            de640_field=soup4.find("subfield",{"code":"z"})
            de640=de640_field.text
            x_data['DE-640']=de640
        except:
            de640="no de640"
            x_data['DE-640']=de640
        xmldata.append(x_data)

def author_search(soup):
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
        print('100:'+author)
        #x_data['author']=author
    except NoneType:
        print('000: no author')
    except:
        author_data=soup.find("datafield",{"tag":"700"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        print('700: '+author_field.text)
    
#df=pd.DataFrame(xmldata)
#df.to_csv("./Python/BWLastCopies/test.csv")
    
time.sleep(0.1)

if __name__=="__main__":
    search()
    print("done")
