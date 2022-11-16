#!/bin/python

from colorama import Fore
import os
import readline
import re
import subprocess
from cmds import help,modules

interance="("+Fore.RED+"lpi"+Fore.WHITE+") > "

def mchecker(md):
   print("["+Fore.GREEN+"+"+Fore.WHITE+"] Module: " + md)
   subprocess.call(["python", "main.py"], cwd="../modules/"+md)

def nf(st,shit):
   if st=="shit":
     stuff="["+Fore.YELLOW+"!"+Fore.WHITE+"] "+Fore.YELLOW+shit+Fore.WHITE+" not found"
     print(stuff)
   else:
     stuff1="["+Fore.RED+"-"+Fore.WHITE+"] no module named "+Fore.YELLOW+shit+Fore.WHITE
     print(stuff1)

def chs():
   choose=input(interance)
   if bool(choose)==False:
      chs()
   else:
      if choose.strip()=="exit":
         exit()
      elif choose.strip()=="help":
         help()
         chs()
      elif choose.strip()=="modules":
         modules()
         chs()
      elif choose.strip()=="clear":
         os.system("clear")
         chs()
      elif "use" in choose:
         arr=[]
         found=False
         module=re.sub(" ","", choose)[3:len(choose)]
         with open('notes/modules.txt') as f:
           arr=list(f)
         for i in range(0,len(arr)):
           if module in arr[i] and len(module.strip()) is len(arr[i].strip()):
             found=True
             break
           else:
             if i==len(arr) and module != arr[i]:
               found=False
             else:
               found=False
         if found is True:
           mchecker(module)
         else:
           nf("",module)
           chs()

      else:
         nf("shit",choose)
         chs()
if __name__ == "__main__":
   chs()
