#!/bin/python

import socket
from colorama import Fore
import time

def run():
   commongateway=["192.168.1.1","192.168.0.1"]
   global lanip
   port = 80
   isGateway=False
   print("["+Fore.BLUE+"*"+Fore.WHITE+"] run...")
   time.sleep(1)
   try:
      lanip=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
   except:
      lanip = None
   if lanip=="127.0.0.1" or lanip=="0.0.0.0" or lanip is None:
      print("["+Fore.RED+"-"+Fore.WHITE+"] please connect to the Wi-Fi")
   else:
      so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      gateway=lanip.split('.')[0]+"."+lanip.split('.')[1]+"."+lanip.split('.')[2]+".1"
      try:
         so.connect((str(gateway), port))
         time.sleep(0.8)
         print("["+Fore.GREEN+"+"+Fore.WHITE+"] "+gateway+" is the gateway")
      except:
         time.sleep(0.8)
         print("["+Fore.RED+"-"+Fore.WHITE+"] we didnt found any gateway make sure you are connected")
