#this is the main file for the program
import logger
from bs4 import BeautifulSoup
import pandas as pd
import variables
from urllib.request import urlopen
import requests
import lxml

log=logger.log()
errmsg_gen="Error, check log/general_log.log for details"
errmsg_api="Error, check log/api_log.log for details"

class bwlastcopies:
    def __init__(self):
        self.titel_path=variables.titel_path
        self.verfasser_path=variables.verfasser_path
        self.api_url_personal=variables.api_url_personal
        self.api_url_general=variables.api_url_general
    
    '''def filecleanup(self): #*only used until aSTEC fixes their csv file encoding
        print("filecleanup")
        title=self.titel_cleanup()
        verfasser=self.verfasser_cleanup()
        #test
        tlen=len(title)
        vlen=len(verfasser)
        if tlen==vlen:
            print("titel and verfasser are equal")
            for i in range(tlen):
                print(title[i],verfasser[i])
        else:
            print("titel and verfasser are not equal")
            print(tlen,vlen)
    def verfasser_cleanup(self): #clean up verfasser file, store in list
        print("verfasser_cleanup")
        with open(self.verfasser_path,encoding='utf-8') as f:
            verfasserdata=f.readlines()
        cleanverfasser=[]
        for line in verfasserdata:
            line=line.replace(" ","%20")
            line=line.replace("\n","")
            line=line.replace("�","?")
            line=line.replace(".","")    
            cleanverfasser.append(line)
        return cleanverfasser
    def titel_cleanup(self): #clean up titel file, store in list 
        with open(self.titel_path,encoding='utf-8') as f:
            titledata=f.readlines()
        cleantitle=[]
        for line in titledata: #replace all symbols that might cause problems with the search
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
            line=line.replace("¬","")
            cleantitle.append(line)
        return cleantitle'''
    def test(self,title,author):
        #print("test")
        #print(title,author)
        #oursearch in test only
        url=self.api_url_personal.replace("{title}",title)
        url=url.replace("{author}",author)
        print(url)
        try:
            result=requests.get(url)        
            if result.status_code==200:
                data=result.text
            symbols=['Ã¶','Ã¼','Ã¤','ÃŸ']
            replacesymbol=['ö','ä','ü','ß']
            for i in range(len(symbols)):
                data=data.replace(symbols[i],replacesymbol[i])
        except:
            print("error")
            log.warning_api("Error: test failed")
            print(errmsg_api)
            exit()
        finally:
            '''
            Fields to search for:
             - title (tag:245,ind1:1,ind2:0,subfield:a)
             - author (tag:100,ind1:1,ind2:0,subfield:a)
             - issues (tag:250,ind1: ,ind2: ,subfield:a)
             - 

            
            '''
            symbols=['Ã¶','Ã¼','Ã¤','ÃŸ']
            replacesymbol=['ö','ä','ü','ß']
            for i in range(len(symbols)):
                data=data.replace(symbols[i],replacesymbol[i])
            soup=BeautifulSoup(data,"lxml")
            #print(soup.prettify())
            #in soup, find {"tag":"250","ind1":" ","ind2":" "} and print contents
            #find the title
            title_field=soup.find_all("datafield",{"tag":"245","ind1":"1","ind2":"0"})
            soup1=BeautifulSoup(str(title_field),"lxml")
            title_field=soup1.find("subfield",{"code":"a"})
            title=title_field.text
            
           

            print(title_field.text)
            #find the author
            author_field=soup.find_all("datafield",{"tag":"100","ind1":"1","ind2":" "})
            soup2=BeautifulSoup(str(author_field),"lxml")
            author_field=soup2.find("subfield",{"code":"a"})
            try:
                print(author_field.text)
            except:
                print("author_field error, fix needed")
            #find the issues
            issues_field=soup.find_all("datafield",{"tag":"250","ind1":" ","ind2":" "},{"subfield code":"a"})
            soup3=BeautifulSoup(str(issues_field),"lxml")
            issues_field=soup3.find("subfield",{"code":"a"})
            value=issues_field.text
            test=value
            if 'Ã¼' in value:
                value=value.replace('Ã¼','ü')
            print(value)
            
            
            '''for field in soup.find_all("datafield",{"tag":"250","ind1":" ","ind2":" "}):
                print(field.text)
            '''
    def xmlextract():
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
            except:
                de640="no de640"
                x_data['DE-640']=de640
            xmldata.append(x_data)
        df=pd.DataFrame(xmldata)
        df.to_csv("./Python/BWLastCopies/test.csv")
   
if __name__=="__main__":
    g=bwlastcopies()
    g.test('Schrödinger programmiert Python','Elter, Stephan')
