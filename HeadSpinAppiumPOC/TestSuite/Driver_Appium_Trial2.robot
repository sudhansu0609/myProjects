*** Settings ***
Resource    ../Resources/Appium_resource.robot
*** Variables ***
${DeviceArg}  NOTE
*** Test Cases ***
# Basic Android App test for video Resolution
    # Check video resolution and speed 
    
Headspin testing of youtube
    [Tags]  
    test youtube on headspin  ${DeviceArg}
    