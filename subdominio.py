import requests  # realizar consultal y peticiones a aplicaciones web
from os import path # determinar si una ruta existe o no existe 
import argparse # permitir mandar parametros a nuestro archivo al momento de ejecutarlo
import sys


#pasar el argumento a parse, obtener el domionio en parser  es decir  argumento(ip ó google.com),, pasamos .-t 192.168.2.6
parser=argparse.ArgumentParser()
parser.add_argument('-t','--target', help='indicar el dominio de la victima')
parser=parser.parse_args() 

def main():
	if parser.target:  #si hay no hay parametro se cierra,, si hay argumento ( -t 192.168.2.6)
		if path.exists('subdominios.txt'): # evaluar si existe un archivo 
			wordlist =open ('subdominios.txt','r') #abrir el archivo y con r leer el archivo txt , 
			                                      #pero solo iguala a la apertura del archivo
			wordlist= wordlist.read().split('\n')#leer por separado con su salto de linea,,  se vee de forma vertical
			for subdominio in wordlist:  #ver de forma vertical cada valor de worlist
				url="http://"+subdominio+"."+parser.target
				try:#intentar hacer algo o sino hacer algo mas
					requests.get(url)#consultar la url
				except requests.ConnectionError:
					pass#pasar
				else:# si no e sun error
					print("(+) Subdominio encontrado"+ url)# si no es un error hare una impresion
             #https
			for subdominio in wordlist:
				url="https://"+subdominio+"."+parser.target
				try:#intentar hacer algo o hacer algo extra
					requests.get(url)#consultar la url
				except requests.ConnectionError:
					pass
				else:# si no es un error
					print("(+) Subdominio encontrado"+ url)# si no es un error hare una impresion
	else:
		print("(+) Ingresa dominio")  
			

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:     #finalizar control +c y no salga error gigante
		sys.exit()

