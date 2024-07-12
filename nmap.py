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
		results=os.popen(consulta).read()
		results=results.split("latency).\n\n")
		results=results[1].split("Nmap done")
		print(results[0])
		
	elif modo==3:
		print("-"*50)
		print(target)
		results=os.popen(consulta).read()
		results=results.split("address (")
		results= results[1].split("ho")
		results=results[0].strip() 

		
        
		if results[0]=="1":
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
		target =input("ingresa ip: ")
		consulta="nmap "+target+mode
		parser(modo,consulta,target)
	else:
		print("Indica el nombre del archivo (e.g ips.txt)")
		archivo=input("=> ")
		file=open(archivo, 'r')
		ips=file.read().split("\n")
		for target in ips:
			consulta="nmap  " +target + mode
			parser(modo,consulta,target) 
			
def main():
	print('bienvenidos a nmap automatizado....')
	time.sleep(1)
	print("Elige un modo de ejecucion...")
	print("[1]. Scan Completo \n[2].Scan light\n[3].Host Disvocery \n[4].Vulnerability Scan \n[5].OS Fingerprinting \n[6].Scan Version \n[#].Salir")
	modo=int(input("=>")) 
	mode=switcher(modo)
	time.sleep(1)
	print("-"*50)
	print("Elige una opcion \n[1].IP\n[2].Lista")
	opcion=int(input("=>"))
	option(opcion,mode, modo) 

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt():
		print("Finalizando.....") 
		sys.exit()
