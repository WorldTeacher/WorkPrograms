import pandas as pd
import os
class Csv:
    """
    This class will create a csv file if it does not exist.

    Args:
        name (str): name of the csv file, without the extension
    """
    def __init__(self,name:str):
        self.name=f'{name}.csv'
        if not os.path.isfile(self.name):
            print("File does not exist, creating file")
            self.create_csv({'title':[],'number of titles':[],'own_issuelist':[],'signatur':[],'owncount':[],'total_issuelist':[],'bibcount':[]})
    def create_csv(self, data:dict):
        """
        This function will create a csv file with the given data.

        Args:
            data (dict): The data to be written to the csv file.
        """
        df=pd.DataFrame(data)
        df.to_csv(self.name)

if __name__ == '__main__':
    a=Csv("nanashi")
    print(a.name)