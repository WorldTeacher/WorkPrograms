import os
import glob
import time
import datetime as dt
from urllib.request import urlopen
import pandas as pd
import xml.etree.ElementTree as ET
import parts
import Python.Searcher.variables as variables
import re

'''
This search function should be able to search both the DNB and K10Plus Databases.
'''
self=1
type=1
#def multi_search():
def multi_search(self,type):
    for file in self.query:
        csvfile=pd.read_csv(file, sep='\t', encoding='uft-8')
        clean_aut=[]
        title=[]
    print('Hello')
        


if __name__=='__main__':
    multi_search(self,type)