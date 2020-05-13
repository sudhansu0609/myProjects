*** Settings ***
Resource    ../Resources/Device_App_Driver.robot


*** Variables ***
${DeviceArg}  A1
*** Test Cases ***
# Basic Android App test for video Resolution
    # Check video resolution and speed 
    
Headspin testing of youtube
    [Tags]  Android
    log to console  ${EXECDIR}
    test youtube on headspin  ${DeviceArg} 

    