#!/usr/bin/env python2

from __future__ import print_function
import sys
import nltk
import nltk.tag.senna

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  for chunk, tag in nltk.tag.senna.CHKTagger('/usr/share/senna-v2.0') \
      .tag(nltk.tokenize.word_tokenize(
      nltk.tokenize.sent_tokenize(f.read())[0])):
    print(chunk, ":", tag)
