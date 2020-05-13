'''
Created on Dec 27, 2018

@author: kumarsis
'''


from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary import SeleniumLibrary
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class restartBrowser():
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
        print ("testing4")
        session_id = seLib.driver.session_id

        return remote_url, session_id  
    
    
    def set_driver_session_id(self,sesion_id):
    #Sets the sessoin_id of the current driver insance to the provided one.'
        seLib = BuiltIn().get_library_instance('SeleniumLibrary')
    
        if seLib.driver.session_id != sesion_id:  # this is pretty much guaranteed to be the case
            seLib.driver.close()  # this closes the session's window
            seLib.driver.quit()  # for remote connections (like ours), this deletes the session, but doesn't stop the SE
    
        # set to the session that's already running
        seLib.driver.session_id = sesion_id 
        
    
    def attach_to_session(self,executor_url, session_id):
        original_execute = WebDriver.execute
        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)
        # Patch the function before creating the driver object
        WebDriver.execute = new_command_execute
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver.session_id = session_id
        # Replace the patched function with original function
        WebDriver.execute = original_execute
        return driver        
