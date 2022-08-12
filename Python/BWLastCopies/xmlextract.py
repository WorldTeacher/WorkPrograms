import pandas as pd
from bs4 import BeautifulSoup
import time
import lxml
xml_file="./Python/BWLastCopies/test.xml"
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
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
        x_data['author']=author
    except:
        author="no author"
        x_data['author']=author

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
        print
    except:
        pass
df=pd.DataFrame(xmldata)
df.to_csv("./Python/BWLastCopies/test.csv")
    
time.sleep(0.1)