#!/usr/bin/env python2

from __future__ import print_function
import MeCab
import sys


def main(*args):
  if len(args) == 0:
    readFile = sys.stdin
  elif len(args) == 1:
    readFile = open(args[0])
  else:
    print("invalid number of arguments")
    return
  
  print(MeCab.Tagger().parse(readFile.read()), end='')

  if len(args) == 1:
    readFile.close()


if __name__ == "__main__":
  main(*sys.argv[1:])
