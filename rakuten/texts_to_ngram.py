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


def nGram(numOfGram, kNode):
  node = kNode
  nGram = ""
  for _ in range(numOfGram):
    if not node.next: # ignore the last meanless word in a sentence
      break
    nGram += node.surface
    node = node.next
  return nGram


def main(*args):
  if len(args) == 3:
    N_GRAM = int(args[1])
    filename = args[2]
  else:
    print("usage: {} <number of grams> <filename>".format(args[0]))
    return
  del args

  nGramIndex = shelve.open(str(N_GRAM) + '_gram_index.db')

  with gzip.open(filename, 'r') as f: # 'rb' or 'rt' for unicode files?
    for line in f:
      fv = {}
      jpSentenceTokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')
      for sentence in [sentence.encode(UTF8) for sentence
          in jpSentenceTokenizer.tokenize(line.decode(UTF8))
          if sentence]:
        tagger = MeCab.Tagger()
        node = tagger.parseToNode(sentence).next
          # ignore the first meanless word
        while node.next: # ignore the last meanless word
          if nGram(N_GRAM, node) not in nGramIndex:
            nGramIndex[nGram(N_GRAM, node)] = len(nGramIndex) + 1
          if nGramIndex[nGram(N_GRAM, node)] in fv:
            fv[nGramIndex[nGram(N_GRAM, node)]] += 1
          else:
            fv[nGramIndex[nGram(N_GRAM, node)]] = 1
          node = node.next
      print(*("{}:{}".format(index, count) for index, count
          in sorted(fv.items())))

  nGramIndex.close()


if __name__ == "__main__":
  main(*sys.argv)
