#!/bin/python

import socket
import time
from colorama import Fore
import sys
sys.path.append( '../../../tools/ssh' ) #ssh
sys.path.append( '../../../tools/ftp' ) #ftp
sys.path.append( '../../../tools/cmd' ) #cmdline
from ssh import connectssh
from ftp import connectftp
from interface import chs

def run(value):
   get = Get()
   get.clear_ports()
   gateway = value[0]
   username = value[1]
   password = value[2]
   # check gateway
   vl=checkgateway(gateway)
   if vl==True:
     time.sleep(1)
     print("["+Fore.GREEN+"+"+Fore.WHITE+"] "+gateway+" is the gateway")
     time.sleep(2)
     yl=checkactiveport(gateway)
     # check ports
     if yl==True:
       time.sleep(0.8)
       print("["+Fore.GREEN+"+"+Fore.WHITE+"] supported port(s) found: " + ' '.join(map(str, get.get_port())))
       time.sleep(2)
       zl=checkdata(gateway, username, password)
       if zl=="wifi":
         time.sleep(0.8)
         print("["+Fore.RED+"-"+Fore.WHITE+"] you are not connected to Wi-Fi")
       else:
         if zl[0]==True and zl[1]==True: #ftp and ssh
           time.sleep(1)
           chs()
         elif zl[0]==True and zl[1]==False: #ftp
           time.sleep(1)
           chs()
         elif zl[0]==False and zl[1]==True: #ssh
           time.sleep(1)
           chs()
         else: 
           time.sleep(1)
     elif yl=="wifi":
       time.sleep(0.8)
       print("["+Fore.RED+"-"+Fore.WHITE+"] you are not connected to Wi-Fi")
     else:
       time.sleep(0.8)
       print("["+Fore.RED+"-"+Fore.WHITE+"] we can't found any supported port")
   elif vl=="wifi":
     time.sleep(1)
     print("["+Fore.RED+"-"+Fore.WHITE+"] you are not connected to Wi-Fi")
   else:
     time.sleep(1)
     print("["+Fore.RED+"-"+Fore.WHITE+"] "+gateway+" is not the gateway")


def connected():
  try:
      bl=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
      return bl
  except:
      return None

def checkdata(gateway, user, passwd):
   bl=connected()
   prts = Get()
   sports = prts.get_port()
   time.sleep(0.5)
   c=[]
   print("["+Fore.BLUE+"*"+ Fore.WHITE +"] use data: [user:"+user+",passwd:"+passwd+"]")
   # check if its connected
   if bl=="127.0.0.1" or bl=="0.0.0.0" or bl is None:
      return "wifi"
   else:
      c.clear()
      for i in range(0,len(sports)):
         if sports[i] == 21:   #ftp
           ftp=connectftp(gateway, user, passwd)
           if ftp is True:
             c.append(True)
           else:
             c.append(False)
         elif sports[i] == 22: #ssh
           ssh=connectssh(gateway, user, passwd)
           if ssh is True:
             c.append(True)
           else:
             c.append(False)
      return c

def checkgateway(gateway):
   bl=connected()
   port = 80
   time.sleep(0.5)
   print("["+Fore.BLUE+"*"+ Fore.WHITE +"] check gateway " + gateway)
   # check if its connected
   if bl=="127.0.0.1" or bl=="0.0.0.0" or bl is None:
      return "wifi"
   else:
      # check gateway
       so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
          so.connect((str(gateway.strip()), port))
          return True
       except:
          return False

def sport():
   return [["ftp",21],["ssh",22]]

def checkactiveport(gateway):
   print("["+Fore.BLUE+"*"+ Fore.WHITE +"] check open ports ")
   # connected
   bl=connected()
   get = Get()
   if bl=="127.0.0.1" or bl=="0.0.0.0" or bl is None:
      return "wifi"
   else:
      port=sport()
      supportedport=[]
      for i in range(0,len(port)):
         so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         try:
            so.connect((str(gateway.strip()), port[i][1]))
            time.sleep(2)
            print("["+Fore.GREEN+"+"+Fore.WHITE+"] port: " + str(port[i][1]) + " <=> " + str(port[i][0]))
            supportedport.append(port[i][1])
            get.set_port(port[i][1])
         except:
            time.sleep(2)
            print("["+Fore.RED+"-"+Fore.WHITE+"] port: " + str(port[i][1]) + " <=> " + port[i][0])
       # check port and return the value
      if len(supportedport)==0:
        return False
      else:
        return True

class Get:
    def __init__(self, port = []):
         self._port = port
    def get_port(self):
        return self._port
    def set_port(self, x):
        self._port.append(x)
    def clear_ports(self):
        self._port.clear()

# to do: check gateway correctly and add cmdline
