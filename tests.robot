*** Settings ***
Library  RfBindings.py
Library  Process

*** Test Cases ***
Testing
    Start Process   python RfBound.py  shell=yes
    Sleep  1 second
    ping
    Terminate All Processes
