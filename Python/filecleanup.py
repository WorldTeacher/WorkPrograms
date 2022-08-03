
#load .txt file
import os
import sys
import shutil
import time
import pandas as pd
file="C:/Users/aky547/GitHub/WorkPrograms/Python/AK.P015906_D20220726_T134325.CSV"
#open file, read contents and store to variable
#if there are errors using the UTF-8 encoding, replace the error with ?
wronglist=[]
dictlist=[]
symbollist=['<','>','!','@','#','$','%','^','&','*','(',')','+','=','{','}','[',']','|','\\',':',';','"','\'',',']
with open(file, 'r', encoding='UTF-8',errors='replace') as f:
    data = f.read()
    data = data.replace('\ufffd', '?')
  
#find all lines that have a ? in them
for line in data.splitlines():
    #if '?' in line:
        
        #print(line)
        for word in line.split(sep=' '):
            #if there is a symbol in the word, which is not in the alphabet or numeric, split it at that point
            for symbol in symbollist:
                if symbol in word:
                    word = word.split(symbol, 1)[0]
                    print(word)
            '''if ';' in word:
                newword=word.split(sep=';')
                for e in newword:
                    if '?' in e:
                        print(e)
                        #wronglist.append(e)
                
                print('split:',word)
                print('newword:',newword)
            #for string in word.split(sep='";"'):
            #print('word: ',word)
            time.sleep(0.5)
            if '?' in word:
                print('replace:',word)
                worddict={'word':word,'replace':'tbd'}
                wronglist.append(word)
                if worddict not in dictlist:
                    dictlist.append(worddict)
                #dictlist.append(worddict)
            #if word == 'f?r'
            #    word.replace('f?r','für')
            #time.sleep(1)
        #time.sleep(10)
#make a dataframe from the list of dictionaries
df=pd.DataFrame(dictlist)
df.to_csv('replace_2.csv',index=False)'''
'''with open(file,'r',errors='',encoding='UTF-8') as f:
    contents = f.read()
#for each line, check if stuff needs to be renamed
for line in contents.splitlines():
    print(line)
    time.sleep(1)'''