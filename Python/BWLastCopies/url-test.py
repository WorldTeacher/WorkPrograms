import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom

def search_records(all_url,pass_issue) -> tuple[list,str]:
    
    r = requests.get(all_url)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        file=r.text
        count=0
        #using minidom to parse xml
        DOMTree = minidom.parseString(file)
        records=DOMTree.getElementsByTagName("record")
        for record in records:
            print(record)
            datafields=record.getElementsByTagName("datafield")
            controlfields=record.getElementsByTagName("controlfield")
            for controlfield in controlfields:
                if controlfield.getAttribute("tag") == "001":
                    print(controlfield.firstChild.data)
            for datafield in datafields:
                print(datafield.getAttribute("tag"))                                 
            #get the number of records
        '''tree=ET.fromstring(file)
        for data in tree.iter('records/record'):
            print(data) '''       

def search_opac_count():
    pass
if __name__ == "__main__":
    #print(urlsearch(title="Java ist auch eine Insel",author="Ullenboom, Christian"))
    #manualsearch(title="Geschichten aus unserer Zeit",author="Hotz, Karl",pass_issue="3. Aufl.")
    #search_our_url("https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DJava%20ist%20auch%20eine%20Insel+and+pica.all%3DUllenboom,%20Christian+and+pica.bib=20735&maximumRecords=10&recordSchema=marcxml")
    search_records("https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3DGeschichten aus unserer Zeit+and+pica.all%3DHotz, Karl+and+pica.bib%3D20735&maximumRecords=100&recordSchema=marcxml",pass_issue="3. Aufl.")
