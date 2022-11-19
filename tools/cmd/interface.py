#!/bin/python

import readline
import subprocess

interance="cmd!> "

def chs():
   choose=input(interance)
   if len(choose) == 0:
     chs()
   elif choose.strip()=="help":
     print("!_please use help()")
   elif choose.strip()=="help()":
     print("help")
   elif choose.strip()=="clear()":
     os.system("clear")
   elif choose.strip()=="exit()":
     exit()
   chs()

if __name__ == "__main__":
   chs()
