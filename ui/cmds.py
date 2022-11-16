#!/bin/python

import subprocess

def reading(file):
   with open(file) as f:
    lines = f.read()
    print(lines)

def help():
   reading("notes/help.txt")

def modules():
   reading("notes/modules.txt")

def back(plc):
   if plc == "term":
     exit()
   else:
     subprocess.call(["python", "term.py"], cwd="../../../ui")
