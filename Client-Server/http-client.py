#!/usr/bin/env python

import httplib
import sys

# Get HTTP server IP
http_server = sys.argv[1]

# Creating a connection
conn = httplib.HTTPConnection(http_server)

while 1:
    cmd = raw_input('input command (ex. GET index.html): ')
    cmd = cmd.split()

    if cmd[0] == 'exit': #tipe exit to end it
        break
    
    # Request command to server
    conn.request(cmd[0], cmd[1])

    # Get response from server
    rsp = conn.getresponse()
    
    #print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)
    
conn.close()
