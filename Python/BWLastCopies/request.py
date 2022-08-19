#testing the api request to include in the main script
import requests
import logger
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import json
import httpx
log=logger.log()
def get_xml(author, title):
    if author == '0':
        #log.info_api(f'Getting xml for {title}')
        url=f'https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}&maximumRecords=10&recordSchema=marcxml'
          
    else:
        #log.info_api(f'Getting xml for {author} and {title}')
        url=f'https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=10&recordSchema=marcxml'
    r = requests.get(url)
    response=httpx.get(url)
    #print(response.text)

    xml = r.text
    count_of_volumes=titlecount(response)
    #print(count_of_volumes)

    #make df from xml
    #print(count_of_volumes)
def titlecount(xml):
    log.info_api('issuecount started')
    soup=BeautifulSoup(xml,"lxml")
    data=soup.find_all("zs")
    print(data)
    #volumecount=soup.find('numberOfRecords')
    #print(volumecount.text)
    #issuecount=soup.find("numberofrecords")
    #return issuecount.text
if __name__=="__main__":
    get_xml(title='Der Ehrliche ist der Dumme',author='Wickert, Ulrich')

    #get_xml(0, 'Java ist auch eine Insel')