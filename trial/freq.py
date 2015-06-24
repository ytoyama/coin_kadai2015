#!/usr/bin/env python3

import sys

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  wordDict = {}
  for word in f.read().split():
    if word in wordDict:
      wordDict[word] += 1
    else:
      wordDict[word] = 1

for word, count in wordDict.items():
  print(word, ":", count)
