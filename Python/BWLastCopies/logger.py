#create logger
import logging
import os

#make sure the log directory exists
#get path
path=os.path.dirname(os.path.abspath(__file__))
#if log directory not in path, add it
if 'log' not in path:
    path=path+'\log'    
#if log directory does not exist, create it
if not os.path.exists(path):
    os.makedirs(path)

class log:
    def __init__(self):
        #create logger for api
        path=os.path.dirname(os.path.abspath(__file__))
        path=path+'\log'
        path=path+'\\'
        self.logger = logging.getLogger('API')
        self.logger.setLevel(logging.DEBUG)
        #create handler
        self.handler = logging.FileHandler(path +'api_log.log')
        self.handler.setLevel(logging.DEBUG)
        #create formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", 
                              "%Y-%m-%d %H:%M:%S")
        self.handler.setFormatter(formatter)
        #add handler to logger
        self.logger.addHandler(self.handler)
        #create logger for general
        self.logger2 = logging.getLogger('General')
        self.logger2.setLevel(logging.DEBUG)
        #create handler
        self.handler2 = logging.FileHandler(path +'general_log.log')
        self.handler2.setLevel(logging.DEBUG)
        #create formatter
        formatter2 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                              "%Y-%m-%d %H:%M:%S")
        self.handler2.setFormatter(formatter2)
        #add handler to logger
        self.logger2.addHandler(self.handler2)
        #create logger for the Database
        self.logger3 = logging.getLogger('Database')
        self.logger3.setLevel(logging.DEBUG)
        #create handler
        self.handler3 = logging.FileHandler(path +'database_log.log')
        self.handler3.setLevel(logging.DEBUG)
        #create formatter
        formatter3 = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                                "%Y-%m-%d %H:%M:%S")
        self.handler3.setFormatter(formatter3)
        #add handler to logger
        self.logger3.addHandler(self.handler3)



    def info_api(self,message):
        self.logger.info(message)
    def error_api(self,message):
        self.logger.error(message)
    def debug_api(self,message):
        self.logger.debug(message)
    def warning_api(self,message):
        self.logger.warning(message)
    def critical_api(self,message):
        self.logger.critical(message)
    def fatal_api(self,message):
        self.logger.fatal(message)
    def info_general(self,message):
        self.logger2.info(message)
    def error_general(self,message):
        self.logger2.error(message)
    def debug_general(self,message):
        self.logger2.debug(message)
    def warning_general(self,message):
        self.logger2.warning(message)
    def critical_general(self,message):
        self.logger2.critical(message)
    def fatal_general(self,message):
        self.logger2.fatal(message)
    def info_database(self,message):
        self.logger3.info(message)
    def error_database(self,message):
        self.logger3.error(message)
    def debug_database(self,message):
        self.logger3.debug(message)
    def warning_database(self,message):
        self.logger3.warning(message)
    def critical_database(self,message):
        self.logger3.critical(message)
    def fatal_database(self,message):
        self.logger3.fatal(message)


