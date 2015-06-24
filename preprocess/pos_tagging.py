#!/usr/bin/env python2

import sys
import nltk
import nltk.tag.senna

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  print(nltk.tag.senna.POSTagger('/usr/share/senna-v2.0')
      .tag(nltk.tokenize.word_tokenize(
      nltk.tokenize.sent_tokenize(f.read())[0])))
