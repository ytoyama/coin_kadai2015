#!/usr/bin/env python3

import sys

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  for word in f.read().split():
    print(word)
