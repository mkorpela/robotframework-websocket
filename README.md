# robotframework-websocket
WebSocket demo for browser library creation

The basic idea is to establish a connection between a webpage on a browser and with a test case
first you need to install the requirements
`pip install -r requirements.txt`
Then you need to start a local server to serve the example webpage
`python -m SimpleHTTPServer 8181`
Then you need to start the test suite (edited) 
`robot tests.robot` (edited) 
And during the first 10 seconds: Open a browser to http://localhost:8181/
What will then happen:
- test has spawned a websocket server
- the browser page will connect to this server
- the test will connect
- the test will send ping commands
- browser page javascript will respond
