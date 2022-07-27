import json
import os
import glob
#find json file
jsonfile=glob.glob('C:\\Users\\aky547\\GitHub\\WorkPrograms\\Python\\BWLastCopies\\*.json',recursive=False)
print(jsonfile[0])
#open config file
with open(jsonfile[0]) as config_file:
   data=json.load(config_file)

titel_path=data['Titel']['Path']
verfasser_path=data['Verfasser']['Path']
namespaces={  # Manually extracted from the XML file, but there could be code written to automatically do that.
            "zs": "http://www.loc.gov/zing/srw/",
            "": "http://www.loc.gov/MARC21/slim",
                }