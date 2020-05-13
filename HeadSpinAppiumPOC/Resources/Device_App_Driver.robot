*** Settings ***

Library           AppiumLibrary
Library           JSONLibrary
Library           OperatingSystem
Library           String
# Library           DynamicXpath     
Library            Collections
Library           pabot.pabotlib
# Library           headspinPythonLib 
Resource          Config_Data_Driver.robot
Resource          Object_Repo_Driver.robot
# Resource          commonKeywords.robot

*** Variables ***

*** Keywords ***
test youtube on headspin
    [Arguments]   ${Device}
  #Set Log Level    None
    # ${username}   common get username
    # ${password}   common get password
    # log to console   username is ${username}
    # log to console   password is ${password}

    ${capabilities_temp}    Get File    ${capability_File_Youtube_${Device}}
    ${capabilitiesFinal}    Convert String to JSON    ${capabilities_temp}
    ${deviceName}           Set Variable    ${capabilitiesFinal}[deviceName]
    ${platformName}         Set Variable    ${capabilitiesFinal}[platformName]

    ${appPackage}           Set Variable    ${capabilitiesFinal}[appPackage]
    ${automationName}       Set Variable    ${capabilitiesFinal}[automationName]
    ${appActivity}          Set Variable    ${capabilitiesFinal}[appActivity]
    ${udid}                 Set Variable    ${capabilitiesFinal}[udid]
     
    Open Application        ${headspinUrl${DEVICE}}    platformName=${platformName}    deviceName=${deviceName}    appPackage=${appPackage}    automationName=${automationName}    appActivity=${appActivity}
    ...    udid=${udid}  
    sleep  2s    
    # log to console  getting library instance
    # ${AppiumLibInstance}=    Get Library Instance  AppiumLibrary  
    
    # log to console  instance is ${AppiumLibInstance}
    # ${driver2}=   Get Webdriver   ${AppiumLibInstance}
     # log to console  driver2 is ${driver2}
   #  DynamicXpath.Get Web Elements   ${driver2}  0
    # log to console   webscraping done
    ${CheckPremium1}   Run Keyword And return status   Wait Until Element Is Visible    ${noThanksOption1}   2s
    Run Keyword And Return If    '${CheckPremium1} '=='True'    Click Element    ${noThanksOption2}

    Click Element           ${search} 

    Sleep    3s
    Input Text              ${searchInput}    ghost stories
 
    Press Keycode           66
    ${searchInputFinal}   Replace String    ${firstVideo}     <textElement>    ${VIDEO_TITLE}    
   
    Wait Until Element Is Visible      ${searchInputFinal}    30s
    Click Element          ${searchInputFinal} 
    :FOR  ${i}  IN RANGE  1 
    \  check Ad and Skip  
    

    Click Element At Coordinates    550    250
    log to console   clicked on screen
      
    #to Pause playing video
    Click Element    ${pauseVideo} 
    #to play paused video
    Wait Until Keyword Succeeds   3x  3   check video is playing
    sleep  3s

    sleep  0.5
    Click Element           ${moreOptionsElement} 
    ${resolution}           Get Element Attribute   ${resolution}     ${ATTRIBUTE_NAME} 
    log to console          resolution is ${resolution}
    log         resolution is ${resolution}
    ${playbackSpeed}        Get Element Attribute   ${playbackSpeedElement}     ${ATTRIBUTE_NAME} 
    log to console          playback speed is ${playbackSpeed}
    log                     playback speed is ${playbackSpeed}
    Click Element At Coordinates    550    250
    Click Element    ${playVideoElement}  
    

    #Release Value Set
check Ad and Skip
    ${ad}   Run Keyword And Return Status    Wait Until Element Is Visible    ${countdownText}     2s
    log to console           checked if add is present
   # sleep   5s   
    Run Keyword If   '${ad}'=='True'  Wait Until Keyword Succeeds   2x  1   Click Element  	         ${adSkipElement}
    
   # sleep    1s
    #${adStatus}             Run Keyword And Return Status	Element Should Be Visible   //android.widget.TextView[contains(@resource-id,'skip')]    5s
check video is playing
    ${currentTime}          Get Element Attribute   ${videoPlaySlideBar}     ${ATTRIBUTE_NAME} 
    @{timeList}             Split String    ${currentTime}   :
    ${timeInSeconds}        Set Variable    @{timeList}[1]
    ${NotplayingStatus}           Run Keyword And Return Status    Should Be Equal As Strings    00    ${timeInSeconds}
    Run Keyword If         '${NotplayingStatus}'=='True'    Fail
    log to console          video is playing    
