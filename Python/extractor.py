#this is a script that extracts the data from the csv file

import time

from urllib.request import Request, urlopen
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import urllib.request
import googlesearch
#import pandas as pd

#open clean_data.csv file with utf-8 encoding
#df = pd.read_csv('clean_data.csv')
#open csv
def google_query(word):
    '''word=str(word.encode('utf-8'))
    #replace \xef with ''
    word=word.replace('\\xef',' ')
    #replace \xbb with ''
    word=word.replace('\\xbb',' ')
    #replace \xbf with ''
    word=word.replace('\\xbf',' ')
    #replace \xbd with ''
    word=word.replace('\\xbd',' ')
    #replace \xbc with ''
    word=word.replace('\\xbc',' ')
    #replace \xbe with ''
    word=word.replace('\\xbe',' ')
    #replace \xba with ''
    word=word.replace('\\xba',' ')
    #replace \xbb with ''
    word=word.replace('\\xbb',' ')
    #replace \xbf with ''
    word=word.replace('\\xbf',' ')
    #replace \xbd with ''
    word=word.replace('\\xbd',' ')
    #replace \xbc with ''
    word=word.replace('\\xbc',' ')
    #replace \xbe with ''
    word=word.replace('\\xbe',' ')
    #replace \xba with ''
    word=word.replace('\\xba',' ')
    #replace \xbb with ''
    word=word.replace('\\xbb',' ')
    #replace \xbf with ''
    word=word.replace('\\xbf',' ')
    #replace \xbd with ''
    word=word.replace('\\xbd',' ')
    #replace \xbc with ''
    word=word.replace('\\xbc',' ')
    #replace \xbe with ''
    word=word.replace('\\xbe',' ')
    #replace \xba with ''
    word=word.replace('\\xba',' ')
    #replace \xbb with ''
    word=word.replace('\\xbb',' ')
    #replace \xbf with ''
    word=word.replace('\\xbf',' ')
    #replace \xbd with ''
    word=word.replace('\\xbd',' ')
    #replace multiple whitespaces with one
    word=word.replace('  ',' ')'''
    articlelist=['�Die�','�Der�','�Das�','�The�']
    if word == 'f�r':
        word = 'für'
    elif word in articlelist:
        word=word.replace('�','')
        print(word)
    else:
        search='"duden+"'+ word
        
        #print(search)
        query='https://www.google.com/search?client=firefox-b-d&q='+search+'&client=google-csbe&output=xml_no_dtd&cx=cx=d168ffb091a06467e'
        print(query)
        openurl=requests.get(query, headers={'User-Agent': 'Mozilla/5.0'},)
        print(openurl.text)
        '''webpage=urlopen(openurl).read()
        #print(webpage)
        print(openurl.text)'''
def cleanup():    
    with open('./Python/clean_data.csv', 'r', encoding='utf-8') as f:
        data=f.readlines()

    for line in data:
        if '�' in line:
            print(line)
            #get every word in the line
            words=line.split()
            #get the index of the word that contains the �
            for word in words:
                if '�' in word:
                    if word == 'f�r':
                        word = 'für'
                        line=line.replace('f�r','für')
                    elif word == '�Die�':
                        word = 'Die'
                        line=line.replace('�Die�','Die')
                    elif word == '�Der�':
                        word = 'Der'
                        line=line.replace('�Der�','Der')
                    elif word == '�Das�':
                        word = 'Das'
                        line=line.replace('�Das�','Das')
                    elif word == '�The�':
                        word = 'The'
                        line=line.replace('�The�','The')
                    else:
                        #get the length of the word
                        wordlen=len(word)
                        #get the position of the �
                        position=word.find('�')+1
                        print('word:', word, 'length:', wordlen, 'position:', position)
                        #google_query(word)
                        time.sleep(2.5)
                        newword =Search_word(word)
                        newword_len=len(newword)
                        # if the length of the new word is shorter than the old word, replace the length of the old word with the new word
                        if newword_len < wordlen:
                            print('new_word:', newword, ',','new_word_length:', newword_len)
                            #replace each letter in the word with the new word
                            
                        else:
                            print(newword)
                            time.sleep(5)
                            #replace the word with the new word
                            line=line.replace(word,newword)
                            print(line)
def Search_word(word): #this function searches for the link to the novels based on the result of get_opf_path()
        
        bslink=""
        query=word #example for testing
        domain='duden' #what page to search on

        lookup=query + " " + domain
        results = search(lookup,num_results=2) #search for the query, and return the first 2 results
        for result in results:
            #if resulting link has /rechtschreibung/ in it, it is the link we want
            if "https://www.duden.de/rechtschreibung/" in result:
                print(result)
                bslink=result
        #open the link and get the html
        with urllib.request.urlopen(bslink) as url:
            html = url.read()
        #parse the html
        soup = BeautifulSoup(html, 'html.parser')
        words =soup.find('span', class_="lemma__main") #looking for span class lemma__main, as this is where the word is stored
        word=words.text
        if '­' in word: #replaces the invisible character, which displays syllabe-separation
            word=word.replace('­','')
        return word

if __name__=="__main__":
    cleanup()
       # google_api_test()