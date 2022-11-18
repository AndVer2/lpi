#!/usr/bin/python

from colorama import Fore
import readline
import sys
sys.path.append( '../../../ui' )
from cmds import back, help, version, table, setter, ccmd
import os
from run import run

interance="("+Fore.RED+"net/exrouter"+Fore.WHITE+") > "
param=["gateway", "user", "pass"]
value=["", "admin", "admin"]
state=["Required", "Required", "Required"]
help=["the gateway of router", "default: admin", "default: password"]

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
      elif choose.strip()=="version":
         version("1")
         chs()
      elif choose.strip()=="show stuff":
         table(param,value,state,help)
         chs()
      elif choose.strip()=="run":
         for i in range(0, len(param)):
            if "Required" == state[i] and value[i] == "":
               print("["+Fore.YELLOW+"!"+Fore.WHITE+"] please set a value for " + param[i])
               break
            elif ("Required" == state[i] and value[i] != "") and i==len(param)-1:
               print("["+Fore.BLUE+"*"+Fore.WHITE+"] run... ")
               run(value)
         chs()
      elif "set" in choose.strip():
         hi=setter(choose.strip())
         if hi=="shit" or hi is None:
           a=""
         else:
           for i in range(0,len(param)):
              if param[i] in hi[0][0] and len(hi[0][0]) == len(param[i]):
                value[i] = hi[0][1]
                print("["+ Fore.GREEN + "+" + Fore.WHITE + "] set " + hi[0][0] + " --> " + value[i])
                break
         chs()
      else:
         nf(choose)
         chs()
if __name__ == "__main__":
   chs()
