#!/usr/bin/env python3

import sys
import os


g_THRESHOLD = 4


def main(*args):
  if len(args) == 2:
    filename = args[1]
  else:
    print("usage: {} <filename>".format(args[0]))
    return
  del args

  with open(filename, 'r') as f:
    lineList = f.readlines()

  os.remove(filename)

  with open(filename, 'w') as f:
    f.writelines(
        str(1 if int(line[:-1]) >= 4 else -1) + '\n'
        for line in lineList)


if __name__ == "__main__":
  main(*sys.argv)
