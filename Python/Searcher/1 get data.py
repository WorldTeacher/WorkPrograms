import pandas as pd
import glob
import os
import variables
import parts

def rm(start):
    for file in start:
        data=pd.read_csv(file, sep="\t",  encoding='utf8')
        data.columns
        #append Data based on rows
        title=[] #this gets all the titles
        for row in data['Titel']:
            title.append(row)
        author=[] #this gets all the authors
        for row in data['Verfasser']:
            author.append(row)
        isbn=[] #this gets all the isbns
        for row in data['ISBN']:
            isbn.append(row)
        df=pd.DataFrame({'Verfasser': author, 'Titel': title, 'ISBN': isbn}) #create new csvs based on extracted data
        #discrading unneeded parts 
        df['ISBN'] = [x.split('; ')[0] for x in data['ISBN']] #discards the second isbn.
        df['Verfasser'] = [x.split('; ')[0] for x in data['Verfasser']] #discards everything after the first author.
        #save csv in set path
        df.to_csv(str(variables.extractReiheA) + os.path.basename(file) + '-extract.csv', sep='\t', encoding='utf8')
        print(file +' saved to ' + variables.extractReiheA)
    parts.rename(variables.extractReiheA)

