#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
  print("usage: {} <filename>".format(sys.argv[0]))
  exit(1)

with open(sys.argv[1], 'r') as openedFile:
  print(openedFile.read())
