
import requests
from bs4 import BeautifulSoup
import lxml
import json
import sys
with open(".\Python\BWLastCopies\BWL\settings.json") as f:
    settings = json.load(f)
bib_id=settings['Bibliotheks-ID']
sigil=settings['Sigel']
def urlsearch(author,title):
    #create the urls based on input title and author, and search them for the required metadata fields 
    
    
    our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{bib_id}&maximumRecords=10&recordSchema=marcxml"
    all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml"
    data={'title':[],'issue':[],'signature':[]}
    try:
        author,issue,signature=search_our_url(our_url)
        data['title'].append(author)
        data['issue'].append(issue)
        data['signature'].append(signature)
        print(data)
    except Exception as e:
        print(e)
        sys.exit()

        #search_all_url(all_url)
def search_our_url(our_url):

    
    r = requests.get(our_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
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
                                                                    
    return author,issue,signature
                        
            
def search_all_url(all_url):
    try:
        r = requests.get(all_url)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            for datafield in soup.find_all("datafield"):
                
                if datafield['tag'] == '250':
                    if "subfield" in str(datafield):
                        for subfield in datafield.find_all("subfield"):
                            print(subfield)
                
        else:
            return "no status code 200"
    except:
        return False

if __name__ == "__main__":
    urlsearch(title="Java ist auch eine Insel",author="Ullenboom, Christian")