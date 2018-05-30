/*1001575625
Neerja Narayanappa*/

In this project, I have learnt to develop a multithreaded Web server and a simple web client. The Web server and Web client communicate using a text-based protocol called HTTP (Hypertext Transfer Protocol). All the programs are written in python v2. All the programs are run and tested on Mac OS using the default terminal and iterm IDE. I have used tmux to efficiently code the programs.

---------------------------------------------------
PROGRAM 1 : Basic Client and Multi Threaded Server
---------------------------------------------------

Execution:

1. Run the server file

python2 server.py

2. Run the client file

python2 client.py localhost README.md

#Passing ReadME.md as the file to be requested


------------------------------------------------------
PROGRAM 2 : Simple HTTP WEB Server
------------------------------------------------------

Execution:

1. Run the server file

sudo python2 http-server.py

2. Run the client file

sudo python2 http-client.py 127.0.0.1

3. Provide the input

ex. GET index.html

-----------------------------------------------------------------------
PROGRAM 3: Simple HTTP Web Server to display the contents on the browser
------------------------------------------------------------------------

Execution:

1. Run the Server file

python2 httpwebserver.py

2. Type the URL onto the browser

http://localhost:8888/
