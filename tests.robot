*** Settings ***
Library  RfBindings.py
Library  Process
Suite Teardown  Terminate All Processes

*** Test Cases ***
Testing Bindings
    Start Process   python RfBound.py  shell=yes
    Sleep  1 second
    ${r}=  ping  joo
    ${r}=  ping  jaa
    ${r}=  ping  jii
    ${r}=  ping  huu
    ${r}=  ping  haa

Testing Remote
    Start Process   python RemotePing.py  shell=yes
    Import Library	Remote  http://127.0.0.1:8270
    ${r}=  pong  joo
    ${r}=  pong  jaa
    ${r}=  pong  jii
    ${r}=  pong  huu
    ${r}=  pong  haa
