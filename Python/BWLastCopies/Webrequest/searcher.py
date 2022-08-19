#import everything for a google search and examination of the results
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

import urllib.request

'''link='https://www.google.com/search?q=duden+Kreuzwortr%EF%BF%BDt&sxsrf=ALiCzsaFSEafbXZmdv4rE6N05I8tonut9w%3A1659511650140&ei=YiPqYqP-B_-X9u8P19ewoAE&ved=0ahUKEwijt6DTkqr5AhX_i_0HHdcrDBQQ4dUDCA0&uact=5&oq=duden+Kreuzwortr%EF%BF%BDt&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjoHCAAQRxCwAzoHCCMQ6gIQJzoECCMQJzoFCAAQkQI6CwguEIAEEMcBENEDOgUIABCABDoFCC4QkQI6CAguENQCEJECOgQIABBDOgUILhCABDoECC4QQzoFCAAQywE6CAguENQCEMsBOgUILhDLAToKCAAQgAQQhwIQFEoECEEYAEoECEYYAFCFD1j8Z2CPamgCcAF4AIABqwGIAdMJkgEDOS40mAEAoAEBoAECsAEKyAEIwAEB&sclient=gws-wiz-serp'
search_result=googlesearch.search(link)
print(search_result)'''

def Search_links(): #this function searches for the link to the novels based on the result of get_opf_path()
        #search_term=self.data
        
        bslink=""
        query='duden' #example for testing
        domain='K�rper' #what page to search, only novelupdates.com is supported, but other sites could be added (PR welcome)
        '''if query=='Python' or query =='HumbleBundle' or query=='Japanese':
            tags=['manual editing needed']
            self.add_tags(tags)'''
        lookup=query + " " + domain
        #print('looking for: ',query)
        results = search(lookup,num_results=2) #search for the query, and return the first 10 results
        #time.sleep(2)
        # displaying the searched result links
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
        #print(soup.prettify())
        #in html, find class class="lemma__main"3
        words =soup.find('span', class_="lemma__main")
        word=words.text
        if '­' in word: #replaces the invisible character, which displays syllabe-separation
            word=word.replace('­','')
        
            
        # if results[1] 
        
if __name__=="__main__":
    Search_links()