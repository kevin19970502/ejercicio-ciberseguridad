
import subprocess 
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('-t','--target', help="Ingresa el sitio web \n (e.g https://ejemplo.com)")
parser=parser.parse_args()

def main():
	if parser.target:
		subprocess.call("wad -u"+parser.target+"> tecnologias.txt", shell=True) 

	else:
		print("(+)Ingresa una URL")

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
		
