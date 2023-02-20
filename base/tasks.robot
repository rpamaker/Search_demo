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
    [Arguments]    ${gmail_account}    ${send_mails}    ${gmail_password}    ${search}
   
    ${articulos}=    Open Web    ${search}
    Enviar mails    ${articulos}    ${gmail_account}    ${send_mails}    ${gmail_password}  
    Close Browser

