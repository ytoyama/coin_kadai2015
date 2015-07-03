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

  parser = CaboCha.Parser('-n 1')

  with open(readFileName, 'r') as readFile:
    tree = parser.parse(readFile.read())
    for i in range(tree.chunk_size()):
      for j in range(
          tree.chunk(i).token_pos,
          tree.chunk(i).token_pos + tree.chunk(i).token_size):
        print(tree.token(j).surface, tree.token(j).ne)
        # B-X : start of a named entity of X
        # I-X : continuation of a named entity of X
        # O : not a named entity


if __name__ == '__main__':
  main(*sys.argv)
