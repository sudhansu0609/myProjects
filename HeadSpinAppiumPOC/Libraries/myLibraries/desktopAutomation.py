from pywinauto.application import  Application, AppStartError
import time
import pywinauto
import pyperclip
#import pyautogui    #--> For Image and Coordinate based Automation.
import os
from pywinauto import ElementNotFoundError
import sys


def killApplication(AppName):
    killCommand="TASKKILL /F /IM "+AppName
    print(killCommand)
    os.system(killCommand)

def LaunchApp(AppPath):
    try:
        app= Application(backend="win32").start(AppPath)    
    except AppStartError as apse:
        print("Invalid Application Path: "+AppPath+". Exception: ",apse)
        sys.exit(1)     #Fails after printing exception
    return app

#     
def SendKeysToDesktopAPP(appObject,appTitleInitials,Value):
    from pywinauto import ElementNotFoundError
    try:
        appTitleInitials='.* '+appTitleInitials
        appInstance=appObject.window(title_re=appTitleInitials)
        appInstance.type_keys(Value)
        appInstance.print_control_identifiers()
    except ElementNotFoundError as enfe:
        print("Element Title: "+appTitleInitials+" not found",enfe)
        sys.exit(1) #Fails after printing exception

def getAppControlIdentifiers(appObject,appTitleInitials):
    from pywinauto import ElementNotFoundError
    try:
        appTitleInitials='.* '+appTitleInitials
        appInstance=appObject.window(title_re=appTitleInitials)
    except ElementNotFoundError as enfe:
        print("Element Title: "+appTitleInitials+" not found",enfe)
        system.exit(1)  #Fails after printing exception
    return appInstance.print_control_identifiers()

def getCopiedItem():
    itemRecieved=pyperclip.paste()
    return itemRecieved    # returns copied item.

def setCopyItem(data):
    data=pyperclip.copy(data)
    return data
    

def keyPress(appObj,keyName):
        window = appObj.top_window()
        window.type_keys(keyName)
#####################Image and Coordinate based Automation:-########################
# def locateImageinScreen(imagePath):
#         try:
#             buttonLocation=pyautogui.locateOnScreen(imagePath)
#             buttonx, buttony = pyautogui.center(buttonLocation)
#         except FileNotFoundError as fnfe:
#             print('Image not found in specified location',fnfe)
#         return buttonx,buttony
# 
# def click_XY_Cordinates(buttonX, buttonY):        
#         pyautogui.click(buttonX, buttonY)
#         
# def write_XY_Cordinates(stringValue):
#         pyautogui.click(buttonX, buttonY)
#         pyautogui.typewrite(stringValue)