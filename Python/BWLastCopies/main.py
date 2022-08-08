#this is the main file for the program
import logger
from bs4 import BeautifulSoup
import pandas as pd
import variables
from urllib.request import urlopen
import requests

log=logger.log()
errmsg_gen="Error, check log/general_log.log for details"
errmsg_api="Error, check log/api_log.log for details"

class bwlastcopies:
    def __init__(self):
        self.titel_path=variables.titel_path
        self.verfasser_path=variables.verfasser_path
        self.api_url_personal=variables.api_url_personal
        self.api_url_general=variables.api_url_general
    
    def filecleanup(self): #*only used until aSTEC fixes their csv file encoding
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
        return cleantitle
    def test(self,title,author):
        #print("test")
        #print(title,author)
        #oursearch in test only
        url=self.api_url_personal.replace("{title}",title)
        url=url.replace("{author}",author)
        #print(url)
        try:
            result=requests.get(url)        
            if result.status_code==200:
                data=result.text
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
            soup=BeautifulSoup(data,"html.parser")
            #print(soup.prettify())
            #in soup, find {"tag":"250","ind1":" ","ind2":" "} and print contents
            #find the title
            '''title_field=soup.find_all("datafield",{"tag":"245","ind1":"1","ind2":"0"})
            soup=BeautifulSoup(str(title_field),"html.parser")
            title_field=soup.find("subfield",{"code":"a"})
            print(title_field.text)'''
            #find the author
            author_field=soup.find_all("datafield",{"tag":"100","ind1":"1","ind2":" "})
            soup=BeautifulSoup(str(author_field),"html.parser")
            author_field=soup.find("subfield",{"code":"a"})
            print(author_field.text)
            #find the issues
            issues_field=soup.find_all("datafield",{"tag":"250","ind1":" ","ind2":" "},{"subfield code":"a"})
            soup=BeautifulSoup(str(issues_field),"html.parser")
            issues_field=soup.find("subfield",{"code":"a"})
            print(issues_field.text)

            
            '''for field in soup.find_all("datafield",{"tag":"250","ind1":" ","ind2":" "}):
                print(field.text)
            '''
              
   
if __name__=="__main__":
    g=bwlastcopies()
    g.test('Java ist auch eine Insel','Ullenboom, Christian')
