#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import shelve
import operator
import os


DEBUG = True

def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


def doc_to_fv(doc_file):
  INDEX_DB_FILE = 'word_index.db'

  wordCount = {}
  wordIndex = shelve.open(INDEX_DB_FILE)

  with open(doc_file) as f:
    debug("processing file,", doc_file)
    for sentence in map(nltk.tokenize.word_tokenize,
              nltk.tokenize.sent_tokenize(f.read())):
      for word in sentence:
        if word in wordCount:
          wordCount[word] += 1
        else:
          wordCount[word] = 1
        if word not in wordIndex:
          wordIndex[word] = len(wordIndex) + 1
  
  featureVector = " ".join(["{}:{}".format(index, wordCount[word])
      for word, index in sorted(wordIndex.items(), key=operator.itemgetter(1))
      if word in wordCount])

  wordIndex.close()

  return featureVector


if __name__ == "__main__":
  assert len(sys.argv) == 2
  print(doc_to_fv(sys.argv[1]))
