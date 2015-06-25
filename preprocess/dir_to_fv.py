#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import os
import os.path
import shelve
import operator

assert len(sys.argv) == 2
assert os.path.isdir(sys.argv[1])

# initialize db
wordCount = shelve.open('word_count.db')
wordIndex = shelve.open('word_index.db')

for item in map(lambda path: os.path.join(sys.argv[1], path),
    os.listdir(sys.argv[1])):
  if os.path.isfile(item):
    with open(item, 'r') as f:
      for sentence in map(nltk.tokenize.word_tokenize,
          nltk.tokenize.sent_tokenize(f.read())):
        for word in sentence:
          assert len(wordCount) == len(wordIndex)
          if word in wordCount:
            assert word in wordIndex
            wordCount[word] += 1
          else:
            assert word not in wordIndex
            wordIndex[word] = len(wordIndex) + 1
            wordCount[word] = 1

print(" ".join(
    ["{}:{}".format(index, wordCount[word])
    for word, index in sorted(wordIndex.items(),
    key=operator.itemgetter(1))]))

# finalize db
wordCount.close()
wordIndex.close()
