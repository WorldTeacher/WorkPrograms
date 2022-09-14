
import requests
from bs4 import BeautifulSoup
import lxml
import json
import sys
from xml.dom import minidom
with open("settings.json") as f:
    settings = json.load(f)
bib_id=settings['Bibliotheks-ID']
sigil=settings['Sigel']
def urlsearch(author,title):
    #create the urls based on input title and author, and search them for the required metadata fields 
    
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=10&recordSchema=marcxml"
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
    data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'all_issues':[],'all_count':[],'DE-640':[]}
    
    #search_our_url(our_url)
    issue,title,signature,ppn=search_our_url(our_url)
    data['title']=title
    data['our_issues']=issue
    data['signature']=signature
    data['ppn']=ppn
    
    print(data)

        #search_all_url(all_url)
def search_our_url(our_url)-> tuple[list,str,str,str,int]:
    print(our_url)
    issuelist=[]
    count=0
    r = requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
    for controlfield in soup.find_all("controlfield"):
        if controlfield['tag'] == '001':
            ppn=controlfield.text
    for datafield in soup.find_all("datafield"):
        #check if datafield 250 exists
        

        if datafield['tag'] == '250': #get all issues
            
            if "subfield" in str(datafield):
                for issues_subfield in datafield.find_all("subfield"):
                    if issues_subfield['code'] == 'a':

                        issue = issues_subfield.text
                        print(issue)
                        if issue not in issuelist:
                            issuelist.append(issue)
        
         
        
        if datafield['tag'] == '245': #get title
            if "subfield" in str(datafield):
                for title_subfield in datafield.find_all("subfield"):
                    if title_subfield['code'] == 'a':
                        title = title_subfield.text
        
        if datafield['tag'] == '924': #get signature, and count how many times the sigil appears
            count+=1
            sigil_count=0
            if "subfield" in str(datafield):
                for signature_subfield in datafield.find_all("subfield"):
                    #if signature_subfield b is the sigil, get subfield g
                    if signature_subfield['code'] == 'b':
                        if signature_subfield.text == sigil:
                            sigil_count+=1
                            for signature_subfield in datafield.find_all("subfield"):
                                if signature_subfield['code'] == 'g':
                                    signature = signature_subfield.text  
    #check issueslist 
    if len(issuelist) == 0:
        issuelist.append("0")
    return issuelist,title,signature,ppn,count

def search_url_xml(our_url) -> int:
    r = requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        #open file while treating it as xml
        file=r.text
        xmldoc = minidom.parseString(file)
        #get number of records
        NoR=xmldoc.getElementsByTagName('zs:numberOfRecords')[0].firstChild.data
        return NoR
                                                       
            
    '''r = requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        <
            #get the number of records
        for number in soup.find_all("numberOfRecords"):
            print(number)

        for datafield in soup.find_all("datafield"):
            
            if datafield['tag'] == '250':
                if "subfield" in str(datafield):
                    for issues_subfield in datafield.find_all("subfield"):
                        if issues_subfield['code'] == 'a':
                            issue = issues_subfield.text
            try:
                if datafield['tag'] == '245':
                    if "subfield" in str(datafield):
                        for author_subfield in datafield.find_all("subfield"):
                            if author_subfield['code'] == 'a':
                                author = author_subfield.text
            except:
                if datafield['tag'] == '700':
                    if "subfield" in str(datafield):
                        for author_subfield in datafield.find_all("subfield"):
                            if author_subfield['code'] == 'a':
                                author = author_subfield.text
            if datafield['tag'] == '924':
                if "subfield" in str(datafield):
                    for signature_subfield in datafield.find_all("subfield"):
                        #if signature_subfield b is the sigil, get subfield g
                        if signature_subfield['code'] == 'b':
                            if signature_subfield.text == sigil:
                                for signature_subfield in datafield.find_all("subfield"):
                                    if signature_subfield['code'] == 'g':
                                        signature = signature_subfield.text                                         
                                                                               
    return author,issue,signature,0'''
                        
            
def search_all_url(all_url) -> tuple[list,str]:
    try:
        r = requests.get(all_url)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            #count=search_url_xml(all_url)
            count=0
            issuelist=[]
            soup = BeautifulSoup(r.text, 'lxml')
            for datafield in soup.find_all("datafield"):
                if datafield['tag'] == '250':
                    if "subfield" in str(datafield):
                        for issues_subfield in datafield.find_all("subfield"):
                            if issues_subfield['code'] == 'a':
                                issue = issues_subfield.text
                                if issue not in issuelist:
                                    issuelist.append(issue)
                
                #get the amount of datafields with tag 924
                if datafield['tag'] == '924':
                    count+=1
            return issuelist,count

                
        else:
            return "no status code 200"
    except:
        return False
#def manual_search(url)
def search_our_ppn(ppn):
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.ppn%3D{ppn}&maximumRecords=10&recordSchema=marcxml"

def manualsearch(author,title) -> dict[str,list]:
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=100&recordSchema=marcxml"
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"
    result_data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'all_issues':[],'all_count':[],'DE-640':[]}
    issue,result_title,signature,ppn,count=search_our_url(our_url)
    
    result_data['title']=result_title
    result_data['our_issues']=issue
    result_data['signature']=signature
    result_data['ppn']=ppn
    result_data['our_count']=count
    all_issues,all_count=search_all_url(all_url)
    result_data['all_issues']=all_issues
    result_data['all_count']=all_count
    print(result_data)
    return result_data

if __name__ == "__main__":
    #print(urlsearch(title="Java ist auch eine Insel",author="Ullenboom, Christian"))
    manualsearch(title="Handbuch Mehrsprachigkeits- und Mehrkulturalitätsdidaktik",author="Fäcke, Christiane")
    #search_our_url("https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DJava%20ist%20auch%20eine%20Insel+and+pica.all%3DUllenboom,%20Christian+and+pica.bib=20735&maximumRecords=10&recordSchema=marcxml")

'''
if datafield['tag'] == '245':
                if "subfield" in str(datafield):
                    for author_subfield in datafield.find_all("subfield"):
                        if author_subfield['code'] == 'a':
                            author = author_subfield.text
                            print(author)
            if datafield['tag'] == '700':
                if "subfield" in str(datafield):
                    for author_subfield in datafield.find_all("subfield"):
                        if author_subfield['code'] == 'a':
                            author = author_subfield.text
                            print(author)
            if datafield['tag'] == '980':
                if "subfield" in str(datafield):
                    for signature_subfield in datafield.find_all("subfield"):
                        #if signature_subfield b is the sigil, get subfield g
                        if signature_subfield['code'] == '9':
                            if signature_subfield.text == '(PHFR)':
                                for signature_subfield in datafield.find_all("subfield"):
                                    if signature_subfield['code'] == 'c':
                                        signature = signature_subfield.text 
                                        print(signature) 
    return author,issue,signature
'''