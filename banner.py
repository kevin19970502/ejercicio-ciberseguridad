import socket # para ejecutar una conexion
import sys   #cierre del programa
import argparse

#pasar el argumento a parse, obtener el domionio en parser
parser=argparse.ArgumentParser()
parser.add_argument('-t','--target', help='indicar el dominio de la victima')
parser=parser.parse_args() 

def banner(IP,port):
	s=socket.socket()# generamos una coneccion
	s.connect((IP,port))#ejecutamos la coneccion
	print (str(s.recv(1024)))# lo que reciva lo va enviar paa nostros leer   --1024 son bit
def main():
	if parser.target:
		IP=parser.target
		port=21
		banner(IP,port)
	else:
		print("(*)Ingresa IP")


if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt():
		sys.exit()
