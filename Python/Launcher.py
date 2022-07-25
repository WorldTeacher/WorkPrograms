

import parts
'''import get_data
import apisearch
import get_data_from_xml
import search_k10plus'''
import Python.Searcher.variables as variables
import os
import glob

'''
def main(path_var, ): #if further coding in here is neccessary, add it here.
    parts.makepath(path_var)
    get_data()
    apisearch()
    get_data_from_xml()
    search_k10plus()
'''

   

#if __name__=='__main__':
#    main(path_var=paths)
parts.makepath(variables.paths)
parts.rm(variables.filelist_1)