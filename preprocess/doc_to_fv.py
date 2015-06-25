#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import shelve
import operator

assert len(sys.argv) == 2

wordCount = shelve.open('word_count.db')
wordIndex = shelve.open('word_index.db')

with open(sys.argv[1]) as f:
  for sentence in map(nltk.tokenize.word_tokenize,
            nltk.tokenize.sent_tokenize(f.read())):
    for word in sentence:
      assert len(wordCount) == len(wordIndex)
      if word in wordCount:
        assert word in wordIndex
        wordCount[word] += 1
      else:
        assert word not in wordIndex
        wordCount[word] = 1
        wordIndex[word] = len(wordIndex) + 1

print(" ".join(
    ["{}:{}".format(index, wordCount[word])
    for word, index in sorted(wordIndex.items(),
    key=operator.itemgetter(1))]))

wordIndex.close()
wordCount.close()
