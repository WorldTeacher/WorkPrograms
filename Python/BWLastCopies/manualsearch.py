import requests
from bs4 import BeautifulSoup
import json
from xml.dom import minidom
from termcolor import colored
with open("settings.json") as f:
    settings = json.load(f)
bib_id=settings['Bibliotheks-ID']
sigil=settings['Sigel']

def search(author, title, pass_issue) -> dict[str,list]:
    if author == '0':
        our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.bib%3D{bib_id}&maximumRecords=100&recordSchema=marcxml"
        all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}&maximumRecords=100&recordSchema=marcxml"
    else:
        our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=100&recordSchema=marcxml"
        all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"

    result_data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'issue_count':[],'DE-640_count':[],'series':[]}
    
    #unsere Daten
    print(f'our_url: {our_url}')
    r=requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code== 200:
        file=r.text
        DOMtree=minidom.parseString(file)
        records=DOMtree.getElementsByTagName('record')
        for record in records:
            data = record.toxml()
            tags_to_check=["245","250","583","830","924"]
            result=(
            BeautifulSoup(data, features="xml")
            .find_all("datafield", tag=tags_to_check)
            )
            #check if datafield 830 is present
            
            for datafield in result:
                if datafield['tag'] == "250" and datafield.find("subfield", code="a").text == pass_issue:
                
                #if datafield['tag'] == "245" and datafield.find("subfield", code="a").text == title:
                    result_data['title']=BeautifulSoup(data,features="xml").find("datafield", tag="245").find("subfield",code="a").text#datafield.find("subfield", code="a").text
                    result_data['ppn']=record.getElementsByTagName('controlfield')[0].firstChild.data
                    #check if datafield 830 is present
                    if datafield['tag'] == "830":
                        result_data['series']="Ja"
                    else:
                        result_data['series']="Nein"	
                    #find all datafields with tag 250
                    issues=(BeautifulSoup(data, features="xml").find_all("datafield", tag="250"))
                    result_data['our_count']=len(issues)
                    for issue in issues:
                        result_data['our_issues']=issue.find("subfield", code="a").text
                    #find all datafields with tag 583
                    lastcopies=(BeautifulSoup(data, features="xml").find_all("datafield", tag="583"))                    
                    lastcopy_store=[]
                    if len(lastcopies) > 0:
                        for lastcopy in lastcopies:
                            #check if subfield z is present
                            if lastcopy.find("subfield", code="z") is not None:
                                lastcopy_store.append(lastcopy.find("subfield", code="z").text)
                        result_data['DE-640_count']=max(lastcopy_store)
                    else:
                        for lastcopy in lastcopies:
                            result_data['DE-640_local']=lastcopy.find("subfield", code="z").text
                    #find all datafields with tag 924 and subfield code b == sigil
                    signature=(BeautifulSoup(data, features="xml").find_all("datafield", tag="924"))
                    for sig in signature:
                        if sig.find("subfield", code="b").text == sigil:
                            result_data['signature']=sig.find("subfield", code="g").text
    #all data
    r_all=requests.get(all_url)
    r_all.encoding = 'utf-8'
    print(r.status_code)
    global_data={'issue':[],'count':[]}
    global_list=[]
    if r_all.status_code==200:
        file_all=r_all.text
        DOMtree_all=minidom.parseString(file_all)
        records_all=DOMtree_all.getElementsByTagName('record')
        for record_all in records_all:
            data_all = record_all.toxml()
            tags_to_check=["250","245","583","830","924"]
            result_all=(
            BeautifulSoup(data_all, features="xml")
            .find_all("datafield", tag=tags_to_check)
            )
            for datafield_all in result_all:
                if datafield_all['tag'] == "245" and datafield_all.find("subfield", code="a").text == title:
                    
                    issues_all=(BeautifulSoup(data_all, features="xml").find_all("datafield", tag="250"))
                    for issue_all in issues_all:
                        global_data['issue']=issue_all.find("subfield", code="a").text
                    count_of_issues=(BeautifulSoup(data_all, features="xml").find_all("datafield", tag="924"))
                    count=len(count_of_issues)
                    global_data['count']=count
                    global_list.append(global_data)
                    global_data={'issue':[],'count':[]}
    counts=len(global_list)
    #sum the count of issues in the global list based on it's length
    global_count=0
    for i in range(counts):
        global_count+=global_list[i]['count']
    result_data['all_count']=sum(global_data['count'])
    print(global_list)
    result_data['all_count']=global_count
    
    text=colored('Our data:', 'blue',attrs=['bold','underline'])
    result_data['issue_count']=create_notification(global_list)
    
    print(f'{text} {result_data}')
    
    return result_data

def create_notification(notification_data)->str:
    notification_length=len(notification_data)
    issues=[]
    counts=[]
    for i in range(notification_length):
        issues.append(notification_data[i]['issue'])
        counts.append(notification_data[i]['count'])
    notilist=[]
    spaces="       "
    for issue, count in zip(issues,counts):
        template=f'\t{spaces}{issue}: {count} \n'
        notilist.append(template)
    notification=''.join(notilist)
    print(notification)
    return notification
    
    
if __name__ == "__main__":
    #search(author="Hotz, Karl", title="Geschichten aus unserer Zeit",pass_issue="3. Aufl.")
    search(author='0',title="Soundcheck",pass_issue="Dr. A, [Nachdr.] - 2003.")