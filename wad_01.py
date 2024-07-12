#verificar si tienes instalado was
# wad permite ver que tecnologias se estan apliacando ejecutando de un servidor web ver tipo servidor

import subprocess # ejecutar comando de cmd
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('-t','--target', help="Ingresa el sitio web \n (e.g https://ejemplo.com)")
parser=parser.parse_args()

def main():
	if parser.target:
		subprocess.call("wad -u"+parser.target+"> tecnologias.txt", shell=True) #ejecutar comando(wad -u(pedir que le pase un parametro)) con run

	else:
		print("(+)Ingresa una URL")

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
		