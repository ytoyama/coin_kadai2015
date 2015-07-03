#!/usr/bin/env python2
# encoding: utf-8

from __future__ import print_function
import nltk
import sys
import gzip


UTF8 = 'utf-8'


def main(*args):
  if len(args) == 2:
    filename = args[1]
  else:
    print("usage: {} <filename>".format(args[0]))
    return
  del args

  jpSentenceTokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')

  with gzip.open(filename, 'r') as f: # 'rb' or 'rt' for unicode files?
    print(*jpSentenceTokenizer.tokenize(f.readline().decode(UTF8)),
          sep='\n')


if __name__ == "__main__":
  main(*sys.argv)
