#!/bin/python

from colorama import Fore
import paramiko

RED=Fore.RED
BLUE=Fore.BLUE
YELLOW=Fore.YELLOW
WHITE=Fore.WHITE

def connect(gateway, user, passwd):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   return ssh.connect(gateway,22,user,passwd)

def connectssh(gateway, user, passwd):
   try:
      connect(gateway,user,passwd)
      print(f"[+] ---Succesfully connect to {gateway} over ssh")
      return True
   except:
      print(f"[-] ---Failed connect to {gateway} over ssh")
      return False
