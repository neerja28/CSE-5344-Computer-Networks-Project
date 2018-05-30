#!/usr/bin/env python

import socket
import sys
import time

host = sys.argv[1]
port = 2828
BUFFER_SIZE = 2048
filename = sys.argv[2]

# Creating a socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

print ('Connection initiated with the server!!!')
# To calculate the time taken for the client-server communication
clock_start = time.clock()
start_time = time.time()

with open('received_file', 'wb') as f:
    while True:
        data = clientsocket.recv(BUFFER_SIZE)
        if not data:
            f.close()
            break
        # writing data onto the file
        f.write(data)

clientsocket.sendall(filename + "\r\n")

print('Successfully recieved the file')
clientsocket.close()
print('Connection Closed')

clock_end = time.clock()
end_time = time.time()

duration_clock = clock_end - clock_start
print 'clock:  start = ',clock_start, ' end = ',clock_end
print 'clock:  duration_clock = ', duration_clock

# Round Trip Time RTT
total_time = end_time - start_time
print 'time:  start = ',start_time, ' end = ',end_time
print 'Round Trip Time = ', total_time
