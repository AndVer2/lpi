#!/bin/python

import subprocess
from colorama import Fore
from tabulate import tabulate
import re

def reading(file):
   with open(file) as f:
    lines = f.read()
    print(lines)

def help(pth):
   reading(pth+"notes/help.txt")

def modules(pth):
   reading(pth+"notes/modules.txt")

def version(v):
   print("v: " + Fore.BLUE + v + Fore.WHITE)

def back(plc):
   if plc == "term":
     exit()
   else:
     subprocess.call(["python", "term.py"], cwd="../../../ui")

def ccmd():
   return ["gateway","port","cmd", "port", "user", "pass"]

def setter(cmd):
   common=ccmd()
   arr=[]
   cmd1=re.sub(" ","", cmd)[3:len(cmd)] #cmdyes
   for i in range(0,len(common)):
      cmd2=cmd1[0:len(common[i])] #cmd
      cmd3=cmd1[len(cmd2):len(cmd1)] #yes
      if cmd2.strip() in common[i] and len(cmd2.strip()) == len(common[i]):
        arr.append([cmd2.strip(),cmd3.strip()])
        return arr
        break
      elif i==len(common)-1 and cmd2.strip() != common[i] and len(common[i]) == len(cmd2.strip()):
          print("["+Fore.YELLOW+"!"+Fore.WHITE+"] "+cmd.strip()[4:len(cmd)]+" is not a legal paramter")
def table(param,value,state,help):
   data=[]
   for i in range(0,len(param)):
      data.append([param[i],value[i],state[i],help[i]])
   col_names = ["Parameter", "Value", "State", "Info"]
   print(tabulate(data, headers=col_names))
   
