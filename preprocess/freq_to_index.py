#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  wordCounter = {}
  wordIndex = {}
  index = 1
  for sentence in map(nltk.tokenize.word_tokenize,
            nltk.tokenize.sent_tokenize(f.read())):
    for word in sentence:
      if word not in wordIndex:
        wordIndex[word] = index
        index += 1
      if word in wordCounter:
        wordCounter[word] += 1
      else:
        wordCounter[word] = 1

for word, count in wordCounter.items():
  print(wordIndex[word], ':', word, ':', count)
