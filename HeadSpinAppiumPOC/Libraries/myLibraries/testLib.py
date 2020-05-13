'''
Created on Nov 3, 2018

@author: kumarsis
'''
import time
import AuthenticationNew 
import subprocess
import base64
from selenium import webdriver

class testLib(object):

    def cpu_info(self):
        #important changed the below line as bytes and string are copnsidered different in python3 and not in python2
       # current_machine_id = base64.b64encode(subprocess.check_output('wmic csproduct get uuid').split('\n')[1].strip())
       try:
          current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode('utf-8').strip('UUID').replace('\n','').strip()
          print("not in exception"+current_machine_id+"line")
       except AttributeError:   
          current_machine_id = subprocess.check_output('wmic csproduct get uuid').strip('UUID').replace('\n','').strip()
          print("in exception"+current_machine_id+"line")
       return current_machine_id
  

    def callAuthentication(self,path):
        
        secret = self.cpu_info()
        secret = (secret).encode('utf-8')      
        cipher2 = AuthenticationNew.AuthenticationNew(secret)
        
        credentials = cipher2.main(path)
        test="abc"
        return credentials
    def create_profile(self,path):
        fp =webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir",path)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/csv')
        fp.update_preferences()
        return fp.path
