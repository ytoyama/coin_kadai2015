#!/usr/bin/env python2
# encoding: utf-8

from __future__ import print_function
import nltk
import sys
import gzip
import MeCab
import shelve


UTF8 = 'utf-8'
WORD_INDEX_FILE = 'word_index.db'


def main(*args):
  if len(args) == 2:
    filename = args[1]
  else:
    print("usage: {} <filename>".format(args[0]))
    return
  del args

  wordIndex = shelve.open('word_index.db')

  with gzip.open(filename, 'r') as f: # which for unicode files, 'rb' or 'rt'?
    for line in f:
      jpSentenceTokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
      fv = {}
      for sentence in [sentence.encode(UTF8) for sentence
          in jpSentenceTokenizer.tokenize(line.decode(UTF8)) if sentence]:
        tagger = MeCab.Tagger()
        node = tagger.parseToNode(sentence).next
          # ignore the first meanless word
        while node.next: # ignore the last meanless word
          if node.surface not in wordIndex:
            wordIndex[node.surface] = len(wordIndex) + 1
          if wordIndex[node.surface] in fv:
            fv[wordIndex[node.surface]] += 1
          else:
            fv[wordIndex[node.surface]] = 1
          node = node.next
    print(*('{}:{}'.format(index, count) for index, count
        in sorted(fv.items()))) # future print function bug in python2

  wordIndex.close()


if __name__ == "__main__":
  main(*sys.argv)
