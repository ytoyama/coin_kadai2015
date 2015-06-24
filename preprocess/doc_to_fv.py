#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import shelve
import operator

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  wordCount = shelve.open('word_count.db')
  wordIndex = shelve.open('word_freq.db')
  for sentence in map(nltk.tokenize.word_tokenize,
            nltk.tokenize.sent_tokenize(f.read())):
    for word in sentence:
      if word not in wordIndex:
        wordIndex[word] = len(wordIndex) + 1
      if word in wordCount:
        wordCount[word] += 1
      else:
        wordCount[word] = 1

assert len(wordCount) == len(wordIndex)
for word, index in sorted(wordIndex.items(), key=operator.itemgetter(1)):
  print("{}:{} {}".format(index, wordCount[word], word))

wordIndex.close()
