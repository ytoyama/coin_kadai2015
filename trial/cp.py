#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
  print("usage: {} <source file> <dest file>".format(sys.argv[0]))
  exit(1)

with open(sys.argv[1], 'r') as srcFile, open(sys.argv[2], 'w') as destFile:
  destFile.write(srcFile.read())
