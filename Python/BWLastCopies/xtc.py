from bs4 import BeautifulSoup
import pandas as pd

class XMLToCSV:
    
    def __init__(self, file_name):
        self.length=self.get_length(file_name)
        #self.make_csv(file_name)

    def get_length(self, file_name):
        with open(file_name,encoding='utf-8') as f:
            data=f.readlines()
            length=len(data)
            return length
    def make_csv(self, file_name):
        with open(file_name,encoding='utf-8') as f:
            data=f.readlines()
            self.length=len(data)
            #print(f'length: {length}')
        xmldata=[]
        for line in data:
            x_data={'title':[],'author':[],'issue':[],'DE-640':[],'signature':[]}
            soup=BeautifulSoup(line,"lxml")
            
            x_data['title']=self.title_search(soup)
            x_data['author']=self.author_search(soup)
            x_data['issue']=self.issue_search(soup)
            x_data['signature']=self.signature_search(soup)
            xmldata.append(x_data)
        df=pd.DataFrame(xmldata)
        #create csv at current directory
        df.to_csv('BWL.csv',index=False,sep='|') # using the pipe (|) as separator, since the data contains commas
    def title_search(self, soup):
        title_data=soup.find("datafield",{"tag":"245"})
        soup1=BeautifulSoup(str(title_data),"lxml")
        title_field=soup1.find("subfield",{"code":"a"})
        soup1=BeautifulSoup(str(title_data),"lxml")
        title_field=soup1.find("subfield",{"code":"a"})
        if title_field is not None:
            title=title_field.text
        else:
            title="0"
        return title
    def author_search(self,soup):
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
    def issue_search(self,soup):
        try:
            issues_data=soup.find("datafield",{"tag":"250"})
            soup3=BeautifulSoup(str(issues_data),"lxml")
            issues_field=soup3.find("subfield",{"code":"a"})
            issues=issues_field.text
        except:
            issues="0"
        return issues
    def signature_search(self,soup):
        try:
            signature_data=soup.find("datafield",{"tag":"852"})
            soup4=BeautifulSoup(str(signature_data),"lxml")
            signature_field=soup4.find("subfield",{"code":"c"})
            signature=signature_field.text
        except:
            signature="0"
        return signature

if __name__ == "__main__":
    xml=XMLToCSV("AK.P006944_D20220727_T155629.XML")
    #xml.make_csv('AK.P006944_D20220727_T155629.XML')
    print(xml.length)

