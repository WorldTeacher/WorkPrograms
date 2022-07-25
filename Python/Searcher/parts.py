import os
import glob
import Python.Searcher.variables as variables
def makepath(path): #makes paths in root folder
    for folder in path:
        if not os.path.exists(folder):
            print('creating path: ' + folder)
            os.makedirs(folder)
        elif os.path.exists(folder):
            print('path already exists: ' + folder)
        else:
            print('path could not be created: ' + folder)


def delete_files(path):
    files=glob.glob(path + '*.csv',recursive=True)
    print('files',files)
    for file in files:
        os.remove(file)


def rename(loc):
    files=glob.glob(loc + '*.csv',recursive=True)
    
    for file in files:
        if loc==variables.extractReiheA:
            os.rename(file, file.replace('.csv-extract.csv', '-extract.csv'))
        elif loc==variables.isbnlist:
            os.rename(file, file.replace('-extract.csv-urllist.csv', '-urllist.csv'))
        elif loc==variables.dnbresult:
            os.rename(file, file.replace('-urllist.csv-additdata.csv', '-additdata.csv'))
        else:
            print('path not found')

       
'''if __name__ == '__main__':
    #rename(var1='./Java/', var2='-extract')
    delete_files(path=input('path to delete: '))
'''
if __name__ == '__main__':
    rename(loc=variables.dnbresult)