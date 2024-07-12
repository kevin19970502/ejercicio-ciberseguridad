import os
import sys
import time

def switcher(opcion):
	if opcion==1:
		nmap_cadena= " -p- -A"
		return nmap_cadena
	elif opcion==2:
		nmap_cadena=" -T5 --top-port 10"
		return nmap_cadena
	elif opcion==3:
		nmap_cadena=" -sn"
		return nmap_cadena
	elif opcion==4:
		nmap_cadena=" --top-ports 100 --script vuln -sV"
		return nmap_cadena
	elif opcion==5:
		nmap_cadena=" -O"
		return nmap_cadena
	elif opcion==6:
		nmap_cadena=" -sV"
		return nmap_cadena
	else:
		print("Finalizando...")
		sys.exit()
def parser (modo,consulta,target):
	if modo==2:
		print("-"*50)
		print(target)
		results=os.popen(consulta).read()##ejecutamos la consulta y leer el resultado
		results=results.split("latency).\n\n")#del resultado convertira la palabra lat4encia en varia y ahi se formara una matriz, realizara salto
		results=results[1].split("Nmap done")#escogeremos la matriz 1,, luego reemplazaremos la palabra mac adress por elemento vacio y se convertira en matriz
		print(results[0])#mostramos de la matriz la posicion0
		
	elif modo==3:
		print("-"*50)
		print(target)
		results=os.popen(consulta).read()##ejecutamos la consulta y leer el resultado
		results=results.split("address (")#resplazamos addre po un seprador      --(al momento de realizar el comando nmap serie de datos inesario en la cabesera eso lo moldemos split) 
		results= results[1].split("ho")# escogemos segunda parte, resplzamos ho por un separador
		results=results[0].strip() #borramos lo espacios(espacio vacios) que hay dentro la matriz results

		
        #al momento realizar el analisis con manp  va salir datos   buscamos dice: 1 host up .. moldeamos moldeamos(split) los datos y ahora solo queda el 1,, esto sale cuando el comando de nmap se ejecuta y encuentra  host
		if results[0]=="1":# al momento que salga resultado del analisis nmap comparamos y es igual 1
			print("(+) El host se encuentra encendido")
		else:
			print("(+) El host se encuentra apagado")
		

	else:
		print("-"*50)
		print(target)
		results=os.system(consulta)

def option(opcion,mode,modo):
	if opcion==1:
		print("Indica la IP (e.g 192.168.0.1)")
		target =input("ingresa ip: ")#recibir la ip que ingresa
		consulta="nmap "+target+mode# completadon el comando de nmap  target= 192.168.0.1, mode = comado (-s -p...)(nmap 192.168.0.1 -p)
		parser(modo,consulta,target)
	else:
		print("Indica el nombre del archivo (e.g ips.txt)")
		archivo=input("=> ")#para obtener un archivo
		file=open(archivo, 'r')#abrimos el archio y leemos(r)
		ips=file.read().split("\n")#leemos el archivo,como son varios datos(ip) separamos los datos
		for target in ips:#recorremos todos los datos separados de archivo y cada y guardamos cada en target
			consulta="nmap  " +target + mode# completadon el comando de nmap  target= 192.168.0.1, mode = comado (-s -p...)(nmap 192.168.0.1 -p)
			parser(modo,consulta,target) #enviamos parametros funcion parser
			
def main():
	print('bienvenidos a nmap automatizado....')
	time.sleep(1)
	print("Elige un modo de ejecucion...")
	print("[1]. Scan Completo \n[2].Scan light\n[3].Host Disvocery \n[4].Vulnerability Scan \n[5].OS Fingerprinting \n[6].Scan Version \n[#].Salir")
	modo=int(input("=>")) #escoger la opcion tipo de escaneo
	mode=switcher(modo)#pasando opciones a funcion switcher y guardanis variable para retornar para luego realizar peticiones
	time.sleep(1)
	print("-"*50)
	print("Elige una opcion \n[1].IP\n[2].Lista")
	opcion=int(input("=>"))#escoger la opcion ip o lista
	option(opcion,mode, modo) # pasaremos a la funcion , valor opcion

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt():
		print("Finalizando.....") #banner mas decente
		sys.exit()
