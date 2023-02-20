*** Settings ***
Documentation   Template robot main suite.
Library         SeleniumLibrary
Library         Collections
Library         libraries/Articulos.py
Library         libraries/SendMails.py



*** Tasks ***
run Task     
    ${articulos}=    Open Web    %{BUSCADOR}
    Enviar mails    ${articulos}    %{gmail_account}    %{send_mails}    %{gmail_password}  
    Close Browser


   


