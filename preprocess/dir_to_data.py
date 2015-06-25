#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import os
import os.path
import shelve
import operator


DEBUG = True

def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


if len(sys.argv) != 3:
  print("usage: {} <label> <directory>".format(sys.argv[0]))
  exit(1)

LABEL = sys.argv[1]
TARGET_DIR = sys.argv[2]

#assert LABEL.isdigit()
assert os.path.isdir(TARGET_DIR)

# initialize db
wordCount = shelve.open('word_count_{}.db'.format(LABEL))
wordIndex = shelve.open('word_index_{}.db'.format(LABEL))

for item in map(lambda path: os.path.join(TARGET_DIR, path),
    os.listdir(TARGET_DIR)):
  if os.path.isfile(item):
    debug("file:", item)
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

print(LABEL, " ".join(
    ["{}:{}".format(index, wordCount[word])
    for word, index in sorted(wordIndex.items(),
    key=operator.itemgetter(1))]))

# finalize db
assert len(wordCount) == len(wordIndex), "when finalizing db"
wordCount.close()
wordIndex.close()
