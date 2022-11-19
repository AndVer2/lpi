#!/bin/python

from colorama import Fore
import ftplib

RED=Fore.RED
BLUE=Fore.BLUE
YELLOW=Fore.YELLOW
WHITE=Fore.WHITE

def connect(gateway, user, passwd):
   return ftplib.FTP(gateway, user, passwd)

def connectftp(gateway, user, passwd):
   try:
      connect(gateway, user, passwd)
      print(f"[+] ---Succesfully connect to {gateway} over ftp")
      return True
   except:
      print(f"[-] ---Failed connect to {gateway} over ftp")
      return False
