'''
Created on Nov 30, 2018

@author: kumarsis SUDHANSU KUMAR SINGH
'''

import  os
from selenium import webdriver
import screenshot
import datetime
import time
import pyautogui

import shutil
ts = None

st = None
st2 = None
logSource = None
print(st)

cwd = os.getcwd()
#screnshots = screenshot.screenshot(cwd)
now = datetime.datetime.now()
st = now.strftime("%Y_%m_%d-%H%M%S")
print(st)
def takeSnapshot(workDir,suiteName,testName):
    print("working dir is "  +workDir)
    print("test name is " +testName)
    
    screnshots = screenshot.screenshot(workDir)
    screnshots.printMyLogs
    finalFolder= screnshots.createFolder(workDir,suiteName,testName)
    print(finalFolder)
    pic = pyautogui.screenshot()
    # Save the image
    #snapPath = finalFolder+"\\"+st
    snapPath = finalFolder
    print("final path is "+snapPath)
    return snapPath
   # pic.save(snapPath+".png") 
    #pic.save(snapPath+".png") 

def copyLogs(workDir,suiteName):
    print("working dir is "  +workDir)
    
    screnshots = screenshot.screenshot(workDir)
    screnshots.printMyLogs
    finalFolder= screnshots.copyLogFile(workDir,suiteName)
    print(finalFolder)
    logSource= workDir+"\\log.html"
    logPath = finalFolder
    print("final path is "+logPath)
    st2=now.strftime("%Y_%m_%d-%H%M%S")
    file = logPath+"\log"+st2
    shutil.copy2(logSource,file+".html")
  

    