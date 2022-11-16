#!/usr/bin/python

import sys

sys.path.append( '../../../ui' )
import cmds

inpu = input("(lpi/gateway) >")

if inpu == "back":
  cmds.back(inpu)
else:
  print("shit")
