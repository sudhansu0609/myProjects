*** Settings ***
Resource    ../Resources/Device_App_Driver.robot


*** Variables ***
${DeviceArg}  Chrome
*** Test Cases ***
# Basic Android App test for video Resolution
    # Check video resolution and speed 
    
Headspin testing of youtube
    [Tags]  Android
    test youtube on headspin  ${DeviceArg} 

    