#!/usr/bin/env python2
# encoding: utf-8

from __future__ import unicode_literals, print_function
import re
import unicodedata
import sys
import gzip


#### The section below from START to END is;
#### from github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja
#### written by hideaki-t (his user name on github.com)
#### START
def unicode_normalize(cls, s):
  pt = re.compile('([{}]+)'.format(cls))

  def norm(c):
    return unicodedata.normalize('NFKC', c) if pt.match(c) else c

  s = ''.join(norm(x) for x in re.split(pt, s))
  return s

def remove_extra_spaces(s):
  s = re.sub('[ 　]+', ' ', s)
  blocks = ''.join(('\u4E00-\u9FFF',  # CJK UNIFIED IDEOGRAPHS
            '\u3040-\u309F',  # HIRAGANA
            '\u30A0-\u30FF',  # KATAKANA
            '\u3000-\u303F',  # CJK SYMBOLS AND PUNCTUATION
            '\uFF00-\uFFEF'  # HALFWIDTH AND FULLWIDTH FORMS
            ))
  basic_latin = '\u0000-\u007F'

  def remove_space_between(cls1, cls2, s):
    p = re.compile('([{}]) ([{}])'.format(cls1, cls2))
    while p.search(s):
      s = p.sub(r'\1\2', s)
    return s

  s = remove_space_between(blocks, blocks, s)
  s = remove_space_between(blocks, basic_latin, s)
  s = remove_space_between(basic_latin, blocks, s)
  return s

def normalize_neologd(s):
  s = s.strip()
  s = unicode_normalize('０−９Ａ-Ｚａ-ｚ｡-ﾟ', s)

  def maketrans(f, t):
    return {ord(x): ord(y) for x, y in zip(f, t)}

  s = s.translate(
    maketrans('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~｡､･｢｣',
          '！”＃＄％＆’（）＊＋，−．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」'))
  s = re.sub('[˗֊‐‑‒–⁃⁻₋−]+', '-', s)   # normalize hyphens
  s = re.sub('[﹣－ｰ—―─━ー]+', 'ー', s)  # normalize choonpus
  s = re.sub('[~∼∾〜〰～]', '', s)  # remove tildes
  s = remove_extra_spaces(s)
  s = unicode_normalize('！”＃＄％＆’（）＊＋，−．／：；＜＞？＠［￥］＾＿｀｛｜｝〜', s)   # keep ＝,・,「,」
  return s
#### END


def main(*args):
  if len(args) == 3:
    srcFilename = args[1]
    destFilename = args[2]
  else:
    print("usage: {} <src_file> <dest_file>".format(args[0]), file=sys.stderr)
    return
  del args

  with gzip.open(srcFilename, 'r') as srcFile, \
      gzip.open(destFilename, 'w') as destFile:
    for line in srcFile:
      destFile.write((normalize_neologd(line) + u'\n').encode('utf-8'))
    #destFile.writelines(normalize_neologd(line).encode('utf-8')
    #                    for line in srcFile)


if __name__ == "__main__":
  main(*sys.argv)
