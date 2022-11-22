from xtc import XMLToCSV as xmlconverter
import requests
from bs4 import BeautifulSoup
import json
from xml.dom import minidom
import make_csv
from search import BookData

'''class AutoSearch:
    def __init__(self):
        # self.length=self.get_length(csv_name)

        pass

    def get_data(self,line):
        line_content = line.split('|')
        title = line_content[0]
        author = line_content[1]
        signature = line_content[4]
        result=(title,author,signature)
        if title == 'title':
            return None
        return result

    def search(self, csv_name, result_csv_name):
        output = []
        csv_file_structure = ['title', 'author', 'signature', '', 'libraries']
        csv_data={'title':[],'author':[],'signature':[],'outside':[]}
        with open(csv_name,encoding="utf-8") as f:
            data = f.readlines()
        for i in range(len(data)):
            #print(data[i])
            if data[i].startswith('title'):
                continue
            title, author,signature = self.get_data(data[i])
            print(title, author)
            csv_data['title']=title
            csv_data['author']=author
            csv_data['signature']=signature
            csv_data['outside']=self.search_outside(title, author)
            output.append(csv_data.copy())
        print(output)        


        make_csv.Csv(result_csv_name).create_csv(output)

    def search_outside(self, title: str, author: str) -> dict:
        # searches the provided api url for the title and author
        # returns a dictionary with the results
        url = f"https://sru.k10plus.de/opac-de-627!rec=1?version=1.1&operation=searchRetrieve&query=pica.tit%3D{title}+and+pica.all%3D{author}&maximumRecords=100&recordSchema=marcxml"
        r = requests.get(url)
        r.encoding = 'utf-8'
        global_data={'issue':[],'count':[],'libraries':[]}
        global_list=[]
        file_all=r.text
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

if __name__ == '__main__':
    # a = AutoSearch()
    # data = a.search_outside(author='Ullenboom, Christian', title="Java ist auch eine Insel")
    # print(data)
    a=AutoSearch().search(csv_name='BWL copy.csv',result_csv_name='test_result_3')'''

class AutoSearch:
    def __init__(self,title,author):
        
        self.title=title
        self.author=author

        pass
    def mass_search(self,):
        

    # def __init__(self):
    #     # self.length=self.get_length(csv_name)

    #     pass

    # def get_data(self,line):
    #     line_content = line.split('|')
    #     title = line_content[0]
    #     author = line_content[1]
    #     signature = line_content[4]
    #     result=(title,author,signature)
    #     if title == 'title':
    #         return None
    #     return result
    
    # def search(self, csv_name, result_csv_name):
    #     with open(csv_name,encoding="utf-8") as f:
    #         data = f.readlines()
    #     for i in range(len(data)):
    #         imput_data=self.get_data(data[i])
    #         if imput_data == None:
    #             continue
    #         title,author,signature=imput_data
    #         print(title,author,signature)
    #         BookData.search(self,title,author)

if __name__ == '__main__':
    a=AutoSearch().search(csv_name='BWL copy.csv',result_csv_name='test_result_3')
