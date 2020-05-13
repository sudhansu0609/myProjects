'''
Created on Nov 26, 2018

@author: kumarsis Sudhansu Kumar Singh
'''
import os
import datetime
import time
ts = None
now = datetime.datetime.now()
st = now.strftime("%Y_%m_%d-%H%M%S")
class screenshot(object):
    '''
    classdocs
    this is to implement screenshot facility in robot in specific folder
    '''


    def __init__(self, destination):
        '''
        Constructor
        '''
        
    def createFolder(self,destination,suite,testCase):
              #now = datetime.datetime.now()
        #st = now.strftime("%Y_%m_%d-%H%M%S")  
        
       # suiteFolder = destination+"\\Execution\\Snapshots\\"+ suite +"\\"+ testCase
        #suiteFolder = destination+"\\Execution\\"+user+"\\Snapshots\\"+ suite
        suiteFolder = destination+"\\Execution\\Snapshots\\"+ suite
        resultFolderFinal = os.path.join(suiteFolder,st)
        print("result fiolder is "+suiteFolder)
        if  not os.path.exists(resultFolderFinal):
            os.makedirs(resultFolderFinal)
        return resultFolderFinal
    
    def copyLogFile(self,destination,suite):

        suiteFolder = destination+"\\Execution\\reportLogs\\"+ suite
        LogFolderFinal = os.path.join(suiteFolder,st)
        print("result fiolder is "+suiteFolder)
        if  not os.path.exists(LogFolderFinal):
            os.makedirs(LogFolderFinal)
        return LogFolderFinal
        
    def printMyLogs(self):
        sampleLogsArray = []
        for entry in self._current_browser().get_log('browser'):
           print(entry)
           sampleLogsArray.append(entry)
             
        
        