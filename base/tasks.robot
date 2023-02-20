*** Settings ***
Documentation   Template robot main suite.
Library         SeleniumLibrary
Library         Collections
Library         libraries/Articulos.py
Library         libraries/SendMails.py



*** Tasks ***
run Task     
    ${articulos}=    Open Web    ${BUSCADOR}
    Enviar mails    ${articulos}    ${send_mails}    ${gmail_password}    ${gmail_account}      
    Close Browser
