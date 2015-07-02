#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import print_function
import MeCab
import sys


# debuggers

DEBUG = True

def debug(*args):
  if DEBUG:
    print(*args, file=sys.stderr)


# main routine

def main(*args):
  if len(args) == 2:
    readFileName = args[1]
  else:
    print("usage: {} <filename>".format(args[0]))
    return

  with open(readFileName, 'r') as readFile:
    # these two lines must be separated because of the bug of MeCab
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(readFile.read()) # no error

    node = node.next # ignore the first meanless word
    while node.next: # ignore the last meanless word
      print(
          node.surface,
          node.feature.split(',')[0],
          node.feature.split(',')[6])
      node = node.next


if __name__ == "__main__":
  main(*sys.argv)
