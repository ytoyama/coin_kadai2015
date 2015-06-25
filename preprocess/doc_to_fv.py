#!/usr/bin/env python2

from __future__ import print_function
import nltk
import sys
import shelve
import operator
import os


def doc_to_fv(doc_file):
  COUNT_DB_FILE = 'word_count.db'
  INDEX_DB_FILE = 'word_index.db'

  wordCount = shelve.open(COUNT_DB_FILE)
  wordIndex = shelve.open(INDEX_DB_FILE)

  with open(doc_file) as f:
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
  
  featureVector = " ".join(["{}:{}".format(index, wordCount[word])
      for word, index in sorted(wordIndex.items(),
      key=operator.itemgetter(1))])
  
  wordCount.close()
  wordIndex.close()

  os.remove(COUNT_DB_FILE)
  os.remove(INDEX_DB_FILE)

  return featureVector


if __name__ == "__main__":
  assert len(sys.argv) == 2
  print(doc_to_fv(sys.argv[1]))
