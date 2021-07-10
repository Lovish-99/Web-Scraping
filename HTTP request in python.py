#Generating the HTTP 'GET' request 

#importing socket module
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))    # In the braces here - "host" of the site is entered.

#making HTTP request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()   # In the braces here - "url" of the site is enterd.

#sending GET request to the servor
mysock.send(cmd)

#Recieving and printing the data from site
while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
