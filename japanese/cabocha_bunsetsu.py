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
    tree = parser.parse(readFile.read())
    #print(dir(tree))
    #print(tree.chunk(0))
    for i in range(tree.chunk_size()):
      for j in range(
          tree.chunk(i).token_pos,
          tree.chunk(i).token_pos + tree.chunk(i).token_size):
        print(tree.token(j).surface, end='')
      print()


if __name__ == '__main__':
  main(*sys.argv)
