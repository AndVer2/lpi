#!/bin/python

import subprocess
from colorama import Fore

def reading(file):
   with open(file) as f:
    lines = f.read()
    print(lines)

def help(pth):
   reading(pth+"notes/help.txt")

def modules():
   reading(pth+"notes/modules.txt")

def version(v):
   print("v: " + Fore.BLUE + v + Fore.WHITE)

def back(plc):
   if plc == "term":
     exit()
   else:
     subprocess.call(["python", "term.py"], cwd="../../../ui")
