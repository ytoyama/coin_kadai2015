#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import os
import os.path
import shelve
import operator
import doc_to_fv


DEBUG = False

def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("usage: {} <label> <directory>".format(sys.argv[0]))
    exit(1)
  
  LABEL = sys.argv[1]
  TARGET_DIR = sys.argv[2]
  assert os.path.isdir(TARGET_DIR)

  map(lambda path: print(LABEL, doc_to_fv.doc_to_fv(path)),
      [item for item in map(lambda path: os.path.join(TARGET_DIR, path),
      os.listdir(TARGET_DIR)) if os.path.isfile(item)])
