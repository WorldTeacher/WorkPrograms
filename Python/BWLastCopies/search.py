
import requests
from bs4 import BeautifulSoup
import json
from xml.dom import minidom
import make_csv

from transformer import CreateNotification as cn

class BookData:
    """
    The BookData class is used to search for a book in the K10plus database.
    It takes the title and the author of the book as arguments.
    Args:
        - title (str): The title of the book.
        - author (str): The author of the book.\n Format: Lastname, Firstname
    """
    def __init__(self,title,author) -> None:
        self.title=title
        if "." in author:
            author=author.replace(".","?")
        self.author=author

        with open("settings.json") as f:
            settings = json.load(f)
        self.bib_id=settings['Bibliotheks-ID']
        self.sigil=settings['Sigel']
        if author == '0':
            self.our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.bib%3D{self.bib_id}&maximumRecords=100&recordSchema=marcxml"
            self.all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}&maximumRecords=100&recordSchema=marcxml"
        else:
            self.our_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}+and+pica.bib%3D{self.bib_id}&maximumRecords=100&recordSchema=marcxml"
            self.all_url=f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"


    def search(self,format=False,iterate=False) -> dict[str,list]:
        """
        This function searches for the specified book in the K10plus database.


        Args:
            - format (bool, optional): Wether or not the resulting data should be formatted in a certain way (mainly for the manual search in the UI). Defaults to False.

        Returns:
            - dict[str,list]: A Dictionary containing the results of the search.
            Content:\n
                - "title": The title of the book.
                - "our_issue": The issue of the book in our library.
                - "signature": The signature of the book in our library.
                - "our_count": The number of issues of the book in our library.
                - "ppn" : The PPN of the book.
                - "issue_count": The number of issues of the book in the K10plus database Formated to: {issue}, {count} | {libraries}.
                - "series": "Ja" if the book is part of a series, "Nein" if not.
                - "all_count": The sum of books returned by the search.
        Example:
        data = BookData("Harry Potter","Rowling, J.K.").search()\n
        """
      
        #unsere Daten
        print(f'our_url: {self.our_url}')
        r=requests.get(self.our_url)
        r.encoding = 'utf-8'
        if r.status_code== 200:
            result_data=self.process_our(r,self.title)
        #all data
        r_all=requests.get(self.all_url)
        r_all.encoding = 'utf-8'
        
        if r_all.status_code==200:
            global_list,global_data=self.process_all(r_all,self.title)
        counts=len(global_list)
        #sum the count of issues in the global list based on it's length
        global_count=0
        for i in range(counts):
            global_count+=global_list[i]['count']
        result_data['all_count']=sum(global_data['count'])
        result_data['all_count']=global_count
        # print(global_list)
        #text=colored('Our data:', 'blue',attrs=['bold','underline'])
        if format==True and iterate==True:
            print("format and iterate")
            noti=cn()
            result_data['issue_count']=noti.create_notification_iterated(global_list)
            return result_data
        if format==True:
            print("format")
            noti=cn()
            result_data['issue_count']=noti.create_notification(global_list)

            return result_data
    
    def process_our(self,r: requests.Response,title) -> dict:
        """Extracts the relevant data from the response of the our url.\n
        Args:
            - r: The response of the our url.
            - title: The title of the book. Used to check if the title is correct.

        Returns:
            - A dictionary containing the relevant data.
        """
        result_data={'title':[],'our_issues':[],'signature':[],'our_count':[],'ppn':[],'issue_count':[],'DE-640_count':[],'series':[]}
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
                if datafield['tag'] == "245" and title in datafield.find("subfield", code="a").text :
                
                #if datafield['tag'] == "245" and datafield.find("subfield", code="a").text == title:
                    result_data['title']=BeautifulSoup(data,features="xml").find("datafield", tag="245").find("subfield",code="a").text#datafield.find("subfield", code="a").text
                    result_data['ppn']=record.getElementsByTagName('controlfield')[0].firstChild.data
                    #check if datafield 830 is present to mark series
                    if BeautifulSoup(data,features="xml").find("datafield", tag="830"):
                        result_data['series']="Ja"
                    else:
                        result_data['series']="Nein"	
                    #find all datafields with tag 250
                    issues=(BeautifulSoup(data, features="xml").find_all("datafield", tag="250"))
                    result_data['our_count']=len(issues)
                    for issue in issues:
                        result_data['our_issues']=issue.find("subfield", code="a").text

                    #if datafield['tag'] == "583" exists, detect last copies value
                    if BeautifulSoup(data, features="xml").find("datafield", tag="583"):
                        lastcopies=(BeautifulSoup(data, features="xml").find_all("datafield", tag="583"))                    
                        lastcopy_store=[]
                        if len(lastcopies) > 0:
                            for lastcopy in lastcopies:
                                #check if subfield z is present
                                if lastcopy.find("subfield", code="z") is not None:
                                    lastcopy_store.append(lastcopy.find("subfield", code="z").text)
                                else:
                                    lastcopy_store.append("0")
                            result_data['DE-640_count']=max(lastcopy_store)
                        else:
                            for lastcopy in lastcopies:
                                result_data['DE-640_count']=lastcopy.find("subfield", code="z").text
                    else:
                        result_data['DE-640_count']=0
                    #find all datafields with tag 924 and subfield code b == sigil
                    signature=(BeautifulSoup(data, features="xml").find_all("datafield", tag="924"))
                    for sig in signature:
                        if sig.find("subfield", code="b").text == self.sigil:
                            result_data['signature']=sig.find("subfield", code="g").text
        return result_data

    def process_all(self,r_all: requests.Response,title:str) -> dict:
        """
        This function extracts the relevant data from the response of the all url.\n

        Args:
            r_all (requests.Response): The response of the all url.
            title (str): The title of the book. Used to check if the title is correct.

        Returns:
            list: A list containing the relevant data.
            dict: A dictionary containing the relevant data.
        """
        global_data={'issue':[],'count':[],'libraries':[]}
        global_list=[]
        file_all=r_all.text
        DOMtree_all=minidom.parseString(file_all)
        records_all=DOMtree_all.getElementsByTagName('record')
        for record_all in records_all:
            libraries_raw=[]
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
                    for count in count_of_issues:
                        libraries_raw.append(count.find("subfield", code="b").text)
                    #remove duplicate entries in libraries_raw
                    libraries=list(set(libraries_raw))
                    global_data['libraries']=libraries
                    count=len(count_of_issues)
                    global_data['count']=count
                    global_list.append(global_data)
                    global_data={'issue':[],'count':[],'libraries':[]}
        return global_list,global_data



if __name__ == "__main__":
    book_data=BookData(title="Java ist auch eine Insel", author="Ullenboom, Christian").search(format=True,iterate=True)
    
    print(book_data)