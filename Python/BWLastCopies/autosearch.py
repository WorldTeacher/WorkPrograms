from xtc import XMLToCSV as xmlconverter
import requests
class AutoSearch:
    def __init__(self):
        
        
        pass
    def search_outside(self, title:str, author:str)->dict:
        #searches the provided api url for the title and author
        #returns a dictionary with the results
        url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"
        r=requests.get(url)
        

if __name__ == '__main__':
    a=AutoSearch()
    a.search_outside("Java ist auch eine Insel","Ullenboom, Christian")