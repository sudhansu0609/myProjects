'''
Created on Dec 27, 2018

@author: kumarsis
'''


from robot.libraries.BuiltIn import BuiltIn
#from  ExtendedSelenium2Library  import  Webdriver
from SeleniumLibrary import SeleniumLibrary
import os
import fileinput
import re
import sys
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class restartModule():
    '''
    classdocs
    '''

# 
#     def __init__(self, driver):
#         '''
#         Constructor
#         '''
   
    

    def return_driver_props(self):
        print("testing1")
        seLib = BuiltIn().get_library_instance('SeleniumLibrary')
        print("testing2")
        #driver=ExtendedSelenium2Library.create_webdriver(chrome, chrome)
        new= BuiltIn().get_library_instance('SeleniumLibrary')
        print("testing3")
        # the driver is instantiated in the SeleniumLibrary, but not provided publicly, thus accessing it through this py code 
        remote_url = seLib.driver.command_executor._url  # for local instance, this is a value in the form 'http://localhost:57856'
        print("testing4")
        session_id = seLib.driver.session_id

        return remote_url, session_id  
    
    
    def attach_browser_new(self,url,session_id):
          print(url)
          print(session_id)
          
          driver = webdriver.Remote(command_executor=url, desired_capabilities={})
          if driver.session_id != session_id:  # this is pretty much guaranteed to be the case
             driver.close() 
             print("driver closed")  # this closes the session's window
             # driver.quit() 
          # driver = webdriver.Remote(url)
          driver.session_id = session_id
          driver.get(url)
         
    def set_driver_session_id(self,sesion_id):
        #driver = webdriver.Chrome()
        print("testing sessionid11")
        
    #Sets the sessoin_id of the current driver insance to the provided one.'
        seLib = BuiltIn().get_library_instance('SeleniumLibrary')
        print("testing sessionid")
       # print    seLib.driver.session_id 
        print(sesion_id)
        if seLib.driver.session_id != sesion_id:  # this is pretty much guaranteed to be the case
            seLib.driver.close() 
            print("driver closed") # this closes the session's window
            seLib.driver.quit() 
           # print  "driver quit" # for remote connections (like ours), this deletes the session, but doesn't stop the SE
     
        # set to the session that's already running
        seLib.driver.session_id = sesion_id 
        
        
    def find_replace(self,file,old,new):
            print(old)
            print(new)
            for line in fileinput.FileInput(file,inplace=1):
                line = re.sub(old,new, line)
                
               # line = line.replace(old,new)
               #print line
                sys.stdout.write(line)
                
    def open_Url(self,txt):
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
       
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        
        capabilities["marionette"] = True
        
        binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
        print("in open url1")
        #driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path='C:/Python37/geckodriver.exe')
        driver = webdriver.Firefox()
#         print("in open url2")
      #  driver.get("http://www.google.com")
    


# executor_url = driver.command_executor._url
# session_id = driver.session_id


        


        
