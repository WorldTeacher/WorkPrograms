
from types import NoneType
import requests
from bs4 import BeautifulSoup
import lxml
import json
import sys
from xml.dom import minidom
from xml.etree import ElementTree as ET
with open("settings.json") as f:
    settings = json.load(f)
bib_id=settings['Bibliotheks-ID']
sigil=settings['Sigel']
def urlsearch(author,title,pass_issue):
    #create the urls based on input title and author, and search them for the required metadata fields 
    
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=10&recordSchema=marcxml"
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
    data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'all_issues':[],'all_count':[],'DE-640':[]}
    
    #search_our_url(our_url)
    issue,title,signature,ppn=search_our_url(our_url,pass_issue)
    data['title']=title
    data['our_issues']=issue
    data['signature']=signature
    data['ppn']=ppn
    
    print(data)

        #search_all_url(all_url)
def search_our_url(our_url,pass_issue)-> tuple[list,str,str,str,int]:
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
        
        if pass_issue != "0":
            if datafield['tag'] == '250': #get all issues
                
                if "subfield" in str(datafield):
                    for issues_subfield in datafield.find_all("subfield"):
                        if issues_subfield['code'] == 'a':
                            if pass_issue in issues_subfield.text:
                                issuelist.append(issues_subfield.text)
                                de640=datafield.find_next("datafield",{"tag":"583"})
                                if "subfield" in str(de640):
                                    for de640_subfield in de640.find_all("subfield"):
                                        if de640_subfield['code'] == 'z':
                                            de640 = de640_subfield.text
                                else: print("no de640")
        else:
            de640=datafield.find_next("datafield",{"tag":"583"})
            if "subfield" in str(de640):
                for de640_subfield in de640.find_all("subfield"):
                    if de640_subfield['code'] == 'z':
                        de640 = de640_subfield.text
            else: print("no de640")
            
        if datafield['tag'] == '245': #get title
            if "subfield" in str(datafield):
                for title_subfield in datafield.find_all("subfield"):
                    if title_subfield['code'] == 'a':
                        title = title_subfield.text
        
        if datafield['tag'] == '924': #get signature, and count how many times the sigil appears
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
    return issuelist,title,signature,ppn,sigil_count,de640
def search_global(datafield):
    pass
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
    
    r = requests.get(all_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        #count=search_url_xml(all_url)
        count=0
        is_list=[]
        issues=[]
        de640l=[]
        soup = BeautifulSoup(r.text, 'lxml')
        for datafield in soup.find_all("datafield"):
            #iterate through all datafields
            #if next datafield is 250, get all issues

            #try:
                
                if datafield['tag'] == '250': #get all issues
                    subfield_a = datafield.find_next("subfield",{"code":"a"})
                    if subfield_a != None:
                        issue=subfield_a.text
                        if issue not in issues:
                            issues.append(issue)
                    #find all datafields with the tag 924 before the next datafield with the tag 250
                    datafield_924 = datafield.find_all("datafield",{"tag":"924"})
                    
                if datafield['tag'] == "583":
                    subfield_z = datafield.find_next("subfield",{"code":"z"})
                    de640=subfield_z.text
                    #if de640 not in de640l:
                    de640l.append(de640)
             
        for issue in issues:
            issuelist={'issue':[],'amount':[],'de640':[]}   
            issuelist['issue'].append(issue)
            issuelist['amount'].append(issues.count(issue))
            issuelist['de640'].append(de640l[0])
            is_list.append(issuelist)
        print(is_list)
        #return issues,count

            
    else:
        print("no status code 200")
    
#def manual_search(url)
def search_our_ppn(ppn):
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.ppn%3D{ppn}&maximumRecords=10&recordSchema=marcxml"
def search_based_on_sto(author,title,pass_issue):
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=100&recordSchema=marcxml"
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"
    result_data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'all_issues':[],'all_count':[],'DE-640_global':[],'DE-640_local':[]}
    print(our_url)
    all_issue=[]
    r = requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        tags_to_check = ["245", "250", "583", "924"]
        data = (
            BeautifulSoup(r.text, features="xml")
            .find_all("datafield", tag=tags_to_check)
        )
        
        for datafield in data:
            subfield_a = datafield.find_next("subfield", {"code": "a"})
            subfield_g = datafield.find_next("subfield", {"code": "g"})
            subfield_z = datafield.find_next("subfield", {"code": "z"})
            if pass_issue != "0":

                if pass_issue in subfield_a:
                    
                    title_data=datafield.find_previous("datafield", {"tag": "245"}) 
                    title=title_data.find_next("subfield", {"code": "a"}).text
                    
                    #print(title, pass_issue)
                    de_640_data=datafield.find_next("datafield", {"tag": "583"})
                    de_640=de_640_data.find_next("subfield", {"code": "z"}).text
                    signature_data=datafield.find_previous("datafield", {"tag": "924"})
                    count=datafield.find_all("datafield", {"tag": "924"})
                    count=len(count)
                    signature=signature_data.find_next("subfield", {"code": "g"}).text
                    #print(de_640, signature)
    
    #global search below this line
    r_all = requests.get(all_url)
    r_all.encoding = 'utf-8'
    if r.status_code == 200:
        tags_to_check = ["245", "250", "583", "924"]
        data_all = (
            BeautifulSoup(r_all.text, features="xml")
            .find_all("datafield", tag=tags_to_check)
        )
        for datafield in data_all:
            subfield_a = datafield.find_next("subfield", {"code": "a"})

            if title in subfield_a:
                #print(datafield) #validate to see if filter works
                all_issues_data=datafield.find_next("datafield", {"tag": "250"})
                try:
                    all_issues=all_issues_data.find_next("subfield", {"code": "a"}).text
                    if all_issues not in all_issue:
                        all_issue.append(all_issues)
                except AttributeError:
                    print("no issues found")
        #use the issue to find how many times the tag 924 is mentioned
        #store the amount in a list
        tags=["245","924"]
        data_len=BeautifulSoup(r_all.text, features="xml").find_all(datafield,tag=tags)
        for datafield in data_len:
            subfield_a=datafield.find_next("subfield",{"code":"a"})
            for issue in all_issue:
                if issue in subfield_a:
                    print(issue)
                    count=data_len.count(data_len.find_next("datafield", {"tag": "924"}))
                    print(count)




    #set data
    result_data['title'].append(title)
    result_data['our_issues'].append(pass_issue)
    result_data['signature'].append(signature)
    result_data['our_count'].append(count)
    result_data['ppn'].append("N/A")
    result_data['all_issues'].append(all_issue)
    print(result_data)
def manualsearch(author,title,pass_issue) -> dict[str,list]:
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=100&recordSchema=marcxml"
    
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"
    result_data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'all_issues':[],'all_count':[],'DE-640_global':[],'DE-640_local':[]}
    issue,result_title,signature,ppn,count,de640=search_our_url(our_url,pass_issue)
    result_data['title']=result_title
    result_data['our_issues']=issue
    result_data['signature']=signature
    result_data['ppn']=ppn
    result_data['our_count']=count
    result_data['DE-640_local']=de640
    '''all_issues,all_count=search_all_url(all_url,pass_issue)
    result_data['all_issues']=all_issues
    result_data['all_count']=all_count'''
    search_all_url(all_url)
    print(result_data)
    return result_data



def search_records(all_url,pass_issue) -> tuple[list,str]:
    
    r = requests.get(all_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        file=r.text
        #using minidom to parse xml
        DOMTree = minidom.parseString(file)
        records=DOMTree.getElementsByTagName("record")
        for record in records:
            datafields=record.getElementsByTagName("datafield")
            for datafield in datafields:
                if datafield.getAttribute("tag") == "250":
                    subfields=datafield.getElementsByTagName("subfield")
                    for subfield in subfields:
                        if subfield.getAttribute("code") == "a":
                            issue=subfield.firstChild.data
                            if issue == pass_issue:
                                print(issue)
                                datafields=record.getElementsByTagName("datafield")
                                for datafield in datafields:
                                    count=0
                                    
                                    if datafield.getAttribute("tag") == "924":
                                        count+=1
                                    if datafield.getAttribute("tag") == "583":
                                        subfields=datafield.getElementsByTagName("subfield")
                                        for subfield in subfields:
                                            if subfield.getAttribute("code") == "z":
                                                de640=subfield.firstChild.data
                                                print(de640)
                                    if datafield.getAttribute("tag") == "924":
                                        #count how many times 924 appears
                                        
                                        subfields=datafield.getElementsByTagName("subfield")
                                        for subfield in subfields:
                                            if subfield.getAttribute("code") == "g":
                                                signature=subfield.firstChild.data
                                                print(signature)
                                                print(count)
            #get the number of records
        '''tree=ET.fromstring(file)
        for data in tree.iter('records/record'):
            print(data) '''       
if __name__ == "__main__":
    #print(urlsearch(title="Java ist auch eine Insel",author="Ullenboom, Christian"))
    #manualsearch(title="Geschichten aus unserer Zeit",author="Hotz, Karl",pass_issue="3. Aufl.")
    #search_our_url("https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DJava%20ist%20auch%20eine%20Insel+and+pica.all%3DUllenboom,%20Christian+and+pica.bib=20735&maximumRecords=10&recordSchema=marcxml")
    #search_records("https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DGeschichten aus unserer Zeit+and+pica.all%3DHotz, Karl+and+pica.bib%3D20735&maximumRecords=100&recordSchema=marcxml",pass_issue="3. Aufl.")
    search_based_on_sto(author="Hotz, Karl", title="Geschichten aus unserer Zeit",pass_issue="3. Aufl.")
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