#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 3:
  print("usage: {} <pattern> <filename>".format(sys.argv[0]))

with open(sys.argv[2]) as openedFile:
  line = openedFile.readline()
  while line:
    if re.search(sys.argv[1], line):
      print(line, end='')
    line = openedFile.readline()
