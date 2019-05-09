*** Settings ***
Library  RfBindings.py
Library  Process
Suite Teardown  Terminate All Processes

*** Test Cases ***
Testing Bindings
    Sleep  10 second
    ${r}=  ping  joo
    ${r}=  ping  jaa
    ${r}=  ping  jii
    ${r}=  ping  huu
    ${r}=  ping  haa
