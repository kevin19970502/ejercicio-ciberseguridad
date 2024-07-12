import socket
import sys
from datetime import datetime

def main():
	target = "192.168.1.133"
	port_min=int(input("Ingresa el puerto menor: "))
	port_max=int(input("Ingresa el puerto mayor: "))
	print ("-"*20)
	print("La IP es :"+target)
	print ("Inicio de escaneos"+str(datetime.now()))
	print("-"*20)
	
	for port in range (port_min,port_max):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) 
		result=s.connect_ex((target,port))
		if result==0:
			print("el puerto {} se encuentra abierto".format(port))
			s.close()
if __name__== '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()		
