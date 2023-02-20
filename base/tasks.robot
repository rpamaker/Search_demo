*** Settings ***
Documentation   Template robot main suite.
Library         SeleniumLibrary
Library         Collections
Library         libraries/ExampleHelper.py
Library         libraries/SendMails.py
Library         libraries/Articulos.py
Resource        keywords/keywords.robot



*** Tasks ***
Example Task
    ${articulos}=    Open Web
    Enviar Mensaje    ${articulos}
    # Close web


*** Keywords ***
Example Keyword
    Open Browser     https://www.mercadolibre.com.uy/    Chrome
    Maximize Browser Window
    Tiempo Espera   


Search
    Input Text    class:nav-search-input    notebook
    Press Enter
    Tiempo Espera 


Scroll In Page
    FOR    ${index}    IN RANGE    10
        Log    ${index}
        scroll
        Tiempo Espera
    END



Close web
        Close Browser
