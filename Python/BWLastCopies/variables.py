import json
import os
import glob
import logger
#find json file
jsonfile=glob.glob('C:\\Users\\aky547\\GitHub\\WorkPrograms\\Python\\BWLastCopies\\config.json',recursive=False)
print(jsonfile[0])
#open config file
log=logger.log()
errmsg_gen="Error, check log/general_log.log for details"
errmsg_api="Error, check log/api_log.log for details"
try:
    with open(jsonfile[0]) as json_file:
        data = json.load(json_file)
        log.info_general("Config file loaded, variables set")
except:
    log.warning_general("Error: Config file not Found, check path")
    print(errmsg_gen)
    
#with open(jsonfile[0]) as config_file:
#  data=json.load(config_file)

titel_path=data['Titel']['Path']
verfasser_path=data['Verfasser']['Path']
titel_test_path=data['Titel-test']['Path']

namespaces={  # Manually extracted from the XML file, but there could be code written to automatically do that.
            "zs": "http://www.loc.gov/zing/srw/",
            "": "http://www.loc.gov/MARC21/slim",
                }