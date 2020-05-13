##wRITTEN BY SUDHANSU KUMAR SINGH
#PLEASE MENTION YOUR NAME IF YOU UPDATE IT
import time
import AuthenticationNew 
import subprocess
import Reporter
class callReporter(object):
    
   
    path = "C:\\SourceCloud\\Robot Automation\\testsuite\\robot\\library\\myLibraries"
    def callCreateFile(self, path):
         report = Reporter.Reporter()
         report.createFile(path)
         
         
    def callApendFile(self,path,KeywordName,expected,actual,imgPath,count):
         report = Reporter.Reporter()
         report.apendFile(path,KeywordName,expected,actual,imgPath,count)

    

