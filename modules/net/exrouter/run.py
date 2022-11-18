#!/bin/python

import socket

def run(value):
   gateway = value[0]
   username = value[1]
   password = value[2]
   # check gateway
   if checkgateway(gateway)==True:
     print("["+Fore.GREEN+"+"+Fore.WHITE+"] "+gateway+" is the gateway")
   else:
     print("["+Fore.RED+"-"+Fore.WHITE+"] "+gateway+" is not the gateway")


def checkgateway(gateway):
   port = 80
   print("[*] check gateway " + gateway)
   # check if its connected
   so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      so.connect((str(gateway.strip()), port))
      return True
   except:
      return False
