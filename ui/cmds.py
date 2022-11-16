#!/bin/python

def reading(file):
   with open(file) as f:
    lines = f.read()
    print(lines)

def help():
   reading("notes/help.txt")

def modules():
   reading("notes/modules.txt")

