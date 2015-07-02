#!/usr/bin/env python3

import sys
import math
import random
import copy
import getopt


# debugger

DEBUG = True
def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)

def fail(message):
  print(message, file=sys.stderr)
  exit(1)

def verbose(message):
  if g_VERBOSE:
    print(message, file=sys.stderr)


# constants

g_AVERAGED_PERCEPTRON = True
g_BIAS = 1
g_NORMALIZE_FV = True
g_MARGIN_THRESHOLD = 0.1
g_UPDATE_NUM = None
g_ONLY_ACCURACY = True
g_VERBOSE = False


# functions

def normalize_fv(fv):
  magnitude = math.sqrt(sum(elem[1] ** 2 for elem in fv))
  return [(elem[0], elem[1] / magnitude) for elem in fv]

def read_instance(line):
  instance = int(line.split()[0]), \
      [(0, g_BIAS)] + [(int(fv_elem.split(':')[0]), int(fv_elem.split(':')[1]))
      for fv_elem in line.split()[1:]]
  if g_NORMALIZE_FV:
    return instance[0], normalize_fv(instance[1])
  else:
    return instance

def read_data(filename):
  with open(filename) as f:
    instances = [read_instance(line)
        for line in f.read().split('\n') if line]
  max_fv_index = -1 # dummy value which must be less than 1
  for instance in instances:
    for fv_elem in instance[1]:
      max_fv_index = max(max_fv_index, fv_elem[0])
  return instances, max_fv_index

def __add_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] += fv_elem[1]

def add_fv(weight, fv, nupdates):
  __add_fv(weight, [(elem[0], nupdates * elem[1]) for elem in fv])

def __sub_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] -= fv_elem[1]

def sub_fv(weight, fv, nupdates):
  __sub_fv(weight, [(elem[0], nupdates * elem[1]) for elem in fv])

def mult_fv(weight, fv):
  assert len(weight) >= len(fv)
  # test data can have indeces larger than weight's max index.
  # so ignore them.
  return sum(weight[elem[0]] * elem[1] for elem in fv if elem[0] < len(weight))

def update_weight(weight, tmp_weight, instance, nupdates):
  iprod = mult_fv(weight, instance[1])
  if (iprod * instance[0] <= 0 or abs(iprod) < g_MARGIN_THRESHOLD) \
      and instance[0] > 0:
    #debug("addition performed.")
    add_fv(weight, instance[1], 1)
    add_fv(tmp_weight, instance[1], nupdates)
  elif (iprod * instance[0] <= 0 or abs(iprod) < g_MARGIN_THRESHOLD) \
      and instance[0] < 0:
    #debug("substruction performed.")
    sub_fv(weight, instance[1], 1)
    sub_fv(tmp_weight, instance[1], nupdates)
  else:
    pass
    #debug("weight was not updated.")

def averaged_weight(weight, tmp_weight, nupdates):
  return [x - y / (nupdates + 1) for x, y in zip(weight, tmp_weight)]

def evaluate(weight, instances):
  num_of_correct_answers = sum(mult_fv(weight, instance[1]) * instance[0] > 0
      for instance in instances)
  return (
        num_of_correct_answers,
        len(instances),
        num_of_correct_answers / len(instances)
      )


# main routine

def main(*args):
  EXEC_NAME = args[0]

  try:
    opts, args = getopt.getopt(args[1:], 'ab:m:nu:v')
  except getopt.GetoptError as err:
    fail(err)
  except:
    fail_unknown()

  try:
    for opt, value in opts:
      if opt in {'-a', '-n'} and value:
        fail("Option, {} does not need any option argument.".format(opt))
      if opt in {'-b', '-m', '-u'} and not value:
        fail("Option, {} needs an option argument.".format(opt))
      if opt == '-a':
        global g_AVERAGED_PERCEPTRON
        g_AVERAGED_PERCEPTRON = False
      elif opt == '-b':
        global g_BIAS
        g_BIAS = float(value)
        if g_BIAS < 0:
          fail("bias for feature vectors cannot be any negative number.")
      elif opt == '-m':
        global g_MARGIN_THRESHOLD
        g_MARGIN_THRESHOLD = float(value)
        if g_MARGIN_THRESHOLD < 0:
          fail("Threshold of margin cannot be any negative number.")
      elif opt == '-n':
        global g_NORMALIZE_FV
        g_NORMALIZE_FV = False
      elif opt == '-u':
        global g_UPDATE_NUM
        g_UPDATE_NUM = int(value)
        if g_UPDATE_NUM <= 0:
          fail("Max num of updates must be a positive number.")
      elif opt == '-v':
        global g_VERBOSE
        g_VERBOSE = True
      else:
        fail("unknown option, {} is detected. (maybe due to programer's error)"
            .format(opt))
  except ValueError as err:
    fail(err)
  except Exception as err:
    fail("Unknown error caught!\n{}".format(err))

  del opts

  if len(args) != 2:
    fail("usage: {} <train data> <test data>".format(EXEC_NAME))

  TRAIN_FILE = args[0]
  TEST_FILE = args[1]
  del args

  if g_UPDATE_NUM == None:
    with open(TRAIN_FILE) as f:
      g_UPDATE_NUM = sum(1 for line in f)
      #debug("g_UPDATE_NUM =", g_UPDATE_NUM)

  # here we go

  random.seed()

  # process train data
  train_instances, train_max_index = read_data(TRAIN_FILE)

  random.shuffle(train_instances)
  weight = [0] * (train_max_index + 1)
  tmp_weight = copy.deepcopy(weight)
  #sum_weight = copy.deepcopy(weight) # DEBUG
  #debug(train_instances)

  for i in range(g_UPDATE_NUM):
    update_weight(
        weight,
        tmp_weight,
        train_instances[i % len(train_instances)],
        i + 1)
    #sum_weight = [sum(x) for x in zip(sum_weight, weight)] # DEBUG
  nupdates = i + 1

  if g_AVERAGED_PERCEPTRON:
    weight = averaged_weight(weight, tmp_weight, nupdates)
  #sum_weight = [x / (nupdates + 1) for x in sum_weight] # DEBUG
  #debug("sum_weight =", sum_weight)
  #debug("ave_weight =", ave_weight)

  # process test data
  test_instances, _ = read_data(TEST_FILE)
  if g_ONLY_ACCURACY:
    print(evaluate(weight, test_instances)[2])
  else:
    print("evaluation result:", *evaluate(weight, test_instances))


if __name__ == "__main__":
  main(*sys.argv)
