#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import os
import os.path
import shelve
import operator

assert len(sys.argv) == 2
assert os.path.isfile(sys.argv[1])

wordDb = shelve.open(sys.argv[1])
map(lambda x: print(*x), sorted(wordDb.items()))
wordDb.close()
