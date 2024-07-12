import socket 
import sys   
import argparse


parser=argparse.ArgumentParser()
parser.add_argument('-t','--target', help='indicar el dominio de la victima')
parser=parser.parse_args() 

def banner(IP,port):
	s=socket.socket()
	s.connect((IP,port))
	print (str(s.recv(1024)))
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
