from bs4 import BeautifulSoup
xml_file="./Python/BWLastCopies/test.xml"
def search():
    with open(xml_file,encoding='utf-8') as f:
        data=f.readlines()
    xmldata=[]
    for line in data:
        x_data={'title':[],'author':[],'issue':[],'DE-640':[]}
        soup=BeautifulSoup(line,"lxml")
        author_search(soup)



def author_search(soup):
    try:
        author_data=soup.find("datafield",{"tag":"100"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        author=author_field.text
        print('100:'+author)
        #x_data['author']=author
    except:
        author_data=soup.find("datafield",{"tag":"700"})
        soup2=BeautifulSoup(str(author_data),"lxml")
        author_field=soup2.find("subfield",{"code":"a"})
        if author_field is not None:
            author=author_field.text
            print('700: '+author)
        #print('700: '+author_field.text)
        else:
            print('no author')

if __name__=="__main__":
    search()