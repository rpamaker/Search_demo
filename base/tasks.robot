*** Settings ***
Documentation   Template robot main suite.
Library         SeleniumLibrary
Library         Collections
Library         libraries/Articulos.py
Library         libraries/SendMails.py



*** Tasks ***
run Task
    run Task

*** Keywords ***
run Task
    [Arguments]    ${recive_env}    ${user_env}    ${passwor_env}
   
    ${articulos}=    Open Web
    Enviar mails    ${articulos}    ${recive_env}    ${user_env}    ${passwor_env}  
    Close Browser

