import socket
import sys
from datetime import datetime

def main():
	target = "192.168.1.133"
	port_min=int(input("Ingresa el puerto menor: "))
	port_max=int(input("Ingresa el puerto mayor: "))
	print ("-"*20)
	print("La IP es :"+target)
	print ("Inicio de escaneos"+str(datetime.now()))#obtenemos la fecha hora convertimos a string para mostralo
	print("-"*20)
	
	for port in range (port_min,port_max):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#SOCKET AF_INET (USAR IPV4), STREAM (usar puerto tcp)
		socket.setdefaulttimeout(1) # tiempo de espera en un segundo se condiera muerto
		result=s.connect_ex((target,port))
		if result==0:
			print("el puerto {} se encuentra abierto".format(port))# formato ingresamos el valor de puerto y lo agregamos dentro de las llaves
			s.close()
if __name__== '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()		
