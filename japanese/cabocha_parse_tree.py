#!/usr/bin/env python2

from __future__ import print_function
import sys
import CaboCha


def main(*args):
  if len(args) == 2:
    readFileName = args[1]
  else:
    print("usage: {} <filename>".format(args[0]), file=sys.stderr)
    return

  parser = CaboCha.Parser()

  with open(readFileName, 'r') as readFile:
    print(parser.parseToString(readFile.read()), end='')


if __name__ == '__main__':
  main(*sys.argv)
