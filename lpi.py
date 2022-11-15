#!/bin/python

import sys
import subprocess

if sys.version_info.major < 3:
    print("lpi supports only Python3. Rerun application in Python3 environment.")
    exit(0)

def hi():
  subprocess.call(["python", "term.py"], cwd="ui")

if __name__ == "__main__":
   hi()
