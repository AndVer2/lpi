#!/usr/bin/python

from colorama import Fore
import readline
import sys
sys.path.append( '../../../ui' )
from cmds import back, help, version, table
from run import run
import os

interance="("+Fore.RED+"net/gateway"+Fore.WHITE+") > "
param=[""]
value=[""]
state=[""]
help=[""]

def nf(shit):
   stuff="["+Fore.YELLOW+"!"+Fore.WHITE+"] "+Fore.YELLOW+shit+Fore.WHITE+" not found"
   print(stuff)

def chs():
   choose=input(interance)
   if bool(choose)==False:
      chs()
   else:
      if choose.strip()=="exit":
         exit()
      elif choose.strip()=="back":
         back(choose)
      elif choose.strip()=="help":
         help("../../../ui/")
         chs()
      elif choose.strip()=="clear":
         os.system("clear")
         chs()
      elif choose.strip()=="run":
         run()
         chs()
      elif choose.strip()=="version":
         version("1")
         chs()
      elif choose.strip()=="show stuff":
         table(param,value,state,help)
         chs()
      else:
         nf(choose)
         chs()
if __name__ == "__main__":
   chs()
