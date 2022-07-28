#create logger
import logging
import logging.handlers
import os

#make sure the log directory exists
if not os.path.exists('log'):
    os.makedirs('log')
class log:
    def __init__(self):
        #create logger for api
        self.logger = logging.getLogger('API')
        self.logger.setLevel(logging.DEBUG)
        #create handler
        self.handler = logging.FileHandler('log/api_log.log')
        self.handler.setLevel(logging.DEBUG)
        #create formatter
        formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
        self.handler.setFormatter(formatter)
        #add handler to logger
        self.logger.addHandler(self.handler)
        #create logger for general
        self.logger2 = logging.getLogger('General')
        self.logger2.setLevel(logging.DEBUG)
        #create handler
        self.handler2 = logging.FileHandler('log/general_log.log')
        self.handler2.setLevel(logging.DEBUG)
        #create formatter
        formatter2 = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
        self.handler2.setFormatter(formatter2)
        #add handler to logger
        self.logger2.addHandler(self.handler2)

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
