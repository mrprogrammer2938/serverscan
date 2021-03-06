#!/usr/bin/python3
# This code write by (ms.nope)
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
serverscan = color.green + "serverscan ~# " + color.white
ip = color.green + "\nEnter ip: " + color.white
time.sleep(1)
os.system("clear")
print(color.green + """

   █▀▀ █▀▀ █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 　 █▀▀ █▀▀ █▀▀█ █▀▀▄ 
   ▀▀█ █▀▀ █▄▄▀ ░█▄█░ █▀▀ █▄▄▀ 　 ▀▀█ █░░ █▄▄█ █░░█ 
   ▀▀▀ ▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀""" + color.red + """\n
                 (🅢🅔🅡🅥🅔🅡 🅢🅒🅐🅝) """ + color.white)

print("[1].scan ip")
print("[2].scan port")
print("[3].Ping Test")
print("[4].Help")
print("[5].Exit")
choose = str(input(serverscan))
if(str(choose) == '1'):
  time.sleep(1)
  os.system("clear")
  print(color.green)
  os.system("figlet serverscan")
  print(color.white)
  webserver = str(input(ip))
  os.system("nmap " + webserver)
  time.sleep(2)
  try3 = str(input("Do you want go to mein menu? [y/n] "))
  if(str(try3) == 'y'):
    os.system("python3 serverscan.py")
  elif(str(try3) == 'n'):
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print("good bye")
      exit(1)
  else:
      time.sleep(1)
      os.system("clear")
      time.sleep(1)
      print(color.red + "Error serverscan" + color.white)
      time.sleep(2)
      try4 = str(input("press Enter... "))
      if(str(try4) == ''):
        os.system("python3 serverscan.py")
      else:
          os.system("python3 serverscan.py")
elif(str(choose) == '2'):
    time.sleep(1)
    os.system("clear")
    print(color.green)
    os.system("figlet portscan")
    print(color.white)
    serverscan2 = str(input(ip))
    time.sleep(1)
    os.system("nmap -Pn " + serverscan2)
    time.sleep(2)
    try8 = str(input("Do you want go to mein menu? [y/n] "))
    if(str(try8) == 'y'):
      os.system("python3 serverscan.py")
    elif(str(try8) == 'n'):
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print("good bye")
        exit(1)
    else:
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print(color.red + "Error serverscan" + color.white)
        time.sleep(2)
        try9 = str(input("press Enter... "))
        if(str(try9) == ''):
          os.system("python3 serverscan.py")
        else:
            os.system("python3 serverscan.py")
    
elif(str(choose) == '3'):
    time.sleep(1)
    os.system("clear")
    print(color.green)
    os.system("figlet pingtest")
    print(color.white)
    serverscan3 = str(input(ip))
    time.sleep(2)
    os.system("ping -w 1 " + serverscan3)
    time.sleep(1)
    try12 = str(input("Do you want go to mein menu? [y/n] "))
    if(str(try12) == 'y'):
      os.system("python3 serverscan.py")
    elif(str(try12) == 'n'):
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print("good bye")
        exit(1)
    else:
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print(color.red + "Error serverscan" + color.white)
        time.sleep(2)
        try13 = str(input("press Enter... "))
        if(str(try13) == ''):
          os.system("python3 serverscan.py")
        else:
            os.system("python3 serverscan.py") 
elif(str(choose) == '4'):
    time.sleep(1)
    os.system("clear")
    print("""
This code write by (ms.nope)
usage:
     1 - and scan ip
     2 - and scan server port
     3 - and start test ping (test conections)
     4 - informtions package(Help)
     5 - Exit package :(
""")
    time.sleep(2)
    try15 = str(input("press Enter... "))
    if(str(try15) == ''):
      os.system("python3 serverscan.py")
    else:
        os.system("python3 serverscan.py")
elif(str(choose) == '5'):
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("good bye")
    exit(1)
elif(str(choose) == ''):
    os.system("python3 serverscan.py")
elif(str(choose) == ' '):
    os.system("python3 serverscan.py")
else:
    time.sleep(1)
    os.system("clear")
    print(color.red + "Error serverscan!" + color.white)
    time.sleep(2)
    try16 = str(input("press Enter... "))
    if(str(try16) == ''):
      os.system("python3 serverscan.py")
    else:
        os.system("python3 serverscan.py")
