import pandas as pd
import os
class Csv:
    def __init__(self,name:str):
        self.name=f'{name}.csv'
        if not os.path.isfile(self.name):
            print("File does not exist, creating file")
            self.create_csv({'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]})
    def create_csv(self, data:dict):
        df=pd.DataFrame(data)
        df.to_csv(self.name)

if __name__ == '__main__':
    a=Csv("nanashi")
    print(a.name)