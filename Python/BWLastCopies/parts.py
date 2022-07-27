import os
import glob
import variables as variables
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


