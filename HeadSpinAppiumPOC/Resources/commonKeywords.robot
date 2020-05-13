*** Settings ***

        
Library             OperatingSystem
Library             String
Library             Screenshot

Library             testLib


*** Variable ***
${textGot}    
${time}             300s
${count}            1
${snapValue}   
${countString}
${elementName} 
${FF_PROFILE}       ${EXECDIR}\\firefoxProfile
${path}             ${EXECDIR}\\robot\\library\\myLibraries
${dash_Line}        =============================================================================================

*** Keywords ***


       
common get username
    [Documentation]   getting usename from encrypted file
    Set Log Level    NONE
    @{credentials}    call Authentication    ${CURDIR}\\..\\properties\\Input
    ${username}       Strip String          @{credentials}[0]                       both
    Log To Console   ${username}
    [Return]         ${username}



common get password
    [Documentation]   getting password value from encrypted file  
    Set Log Level    NONE
    @{credentials}    call Authentication    ${CURDIR}\\..\\properties\\Input
    ${password}=      Strip String          @{credentials}[1]                       both
    [Return]          ${password}


common get itservices password 
     Set Log Level    NONE
    @{credentials}    call Authentication    ${CURDIR}\\..\\properties\\Input
    ${itServicesPassword}=      Strip String          @{credentials}[2]                       both
    [Return]          ${itServicesPassword}


common get rsa Pin 
    Set Log Level    NONE
    @{credentials}    call Authentication    ${CURDIR}\\..\\properties\\Input
    ${pin} =      Strip String          @{credentials}[3]                       both
    [Return]          ${pin}        


common get Test itServices Password 
     Set Log Level    NONE
    @{credentials}    call Authentication    ${CURDIR}\\..\\properties\\Input
    ${testItServices}=      Strip String          @{credentials}[4]                       both
    [Return]          ${testItServices}        





Authentication
    [Documentation]      This Keyword Encripts and Decripts the Credentials Supplied by the User.
    # log to console    test1
    ${userid}        common get username
    ${password}      common get password  
    Set Global Variable    ${GLOBAL_USERID}    ${userid}     
    Set Global Variable    ${GLOBAL_PWD}       ${password}   
