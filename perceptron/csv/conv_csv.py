#!/usr/bin/env python2

from __future__ import print_function
import sys
import os
import os.path
import csv
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# debugger

DEBUG = True

def debug(*args):
  if DEBUG:
    error(*args)

def error(*args):
  print(*args, file=sys.stderr)


# functions

def isCsv(filename):
  return bool(re.search(r".csv$", filename))


def main(*args):
  if len(args) == 3:
    srcDir = args[1]
    targetDir = args[2]
  else:
    error("usage: {} <source directory> <target directory>".format(args[0]))
    return
  del args

  result = {}
  for filename in os.listdir(srcDir):
    if os.path.isfile(filename) and isCsv(filename):
      #debug(filename)
      nIter, name = os.path.splitext(filename)[0].split('-')
      #debug(nIter, name)
      nIter = int(nIter)
      if name not in result:
        result[name] = {}
      assert nIter not in result[name]
      with open(filename) as f:
        result[name][nIter] \
            = [(float(x), float(y)) for x, y in list(csv.reader(f))]
  #debug(result)

  totalResult = {}
  for name, iteratedCsv in sorted(result.items()):
    #debug(iteratedCsv.items())
    totalResult = [(x, 0) for x, y in iteratedCsv.items()[0][1]]
    for _, xy in iteratedCsv.items():
      #debug(totalResult)
      #debug(xy)
      assert len(totalResult) == len(xy)
      totalResult = [(resultTuple[0], resultTuple[1] + xyTuple[1])
          for resultTuple, xyTuple in zip(totalResult, xy)]
    totalResult = [(x, y / len(result[name])) for x, y in totalResult]
    debug(name, totalResult)

    # create image file of graph
    fig = plt.figure(0)
    plt.clf()
    plt.xlabel("value of " + name + " option")
    plt.ylabel("accuracy")
    plt.grid()
    plt.plot([x for x, _ in totalResult], [y for _, y in totalResult])
    fig.savefig(os.path.join(targetDir, name + ".png"))


if __name__ == "__main__":
  main(*sys.argv)
