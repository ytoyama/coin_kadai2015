#!/usr/bin/env python3

import sys
import math
import random
import copy


# debugger

DEBUG = True
def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


# constants

RANDOM_SEED = 12345
IPROD_THRESHOLD = 0.1


# functions

def normalize_fv(fv):
  magnitude = math.sqrt(sum(elem[1] ** 2 for elem in fv))
  return [(elem[0], elem[1] / magnitude) for elem in fv]

def read_instance(line):
  return (int(line.split()[0]), normalize_fv([(0, 1)]
      + [(int(fv_elem.split(':')[0]), int(fv_elem.split(':')[1]))
      for fv_elem in line.split()[1:]]))

def read_data(filename):
  with open(filename) as f:
    instances = [read_instance(line)
        for line in f.read().split('\n') if line]
  return (instances, max(len(instance[1]) - 1 for instance in instances))
  # instance[1] - 1 is for max index of data itself (without bias term)

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
  return sum(x * y[1] for x, y in zip(weight, fv))

def update_weight(weight, tmp_weight, instance, nupdates):
  iprod = mult_fv(weight, instance[1])
  if (iprod * instance[0] <= 0 or abs(iprod) < IPROD_THRESHOLD) \
      and instance[0] > 0:
    #debug("addition performed.")
    add_fv(weight, instance[1], 1)
    add_fv(tmp_weight, instance[1], nupdates)
  elif (iprod * instance[0] <= 0 or abs(iprod) < IPROD_THRESHOLD) \
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

def main():
  assert len(sys.argv) == 3, \
      "usage: {} <train data> <test data>".format(sys.argv[0])

  random.seed(RANDOM_SEED)

  # process train data
  train_instances, train_max_index = read_data(sys.argv[1])


  #random.shuffle(train_instances)
  weight = [0] * (train_max_index + 1)
  tmp_weight = copy.deepcopy(weight)
  sum_weight = copy.deepcopy(weight) # DEBUG
  nupdates = 0
  #debug(train_instances)

  for instance in train_instances:
    nupdates += 1
    #debug("nupdates =", nupdates)
    update_weight(weight, tmp_weight, instance, nupdates)
    #debug("weight =", weight)
    #debug("tmp_weight =", tmp_weight)
    sum_weight = [sum(x) for x in zip(sum_weight, weight)] # DEBUG
    #debug("sum_weight =", sum_weight)

  sum_weight = [x / (nupdates + 1) for x in sum_weight]
  ave_weight = averaged_weight(weight, tmp_weight, nupdates)
  #debug("sum_weight =", sum_weight) # DEBUG
  #debug("ave_weight =", ave_weight)
  #debug("weight =", weight)
  #debug("tmp_weight =", tmp_weight)

  # process test data
  test_instances, test_max_index = read_data(sys.argv[2])
  print("evaluation result:", *evaluate(weight, test_instances))

  #if DEBUG:
  #  debug(train_data[0])
  #  add_fv(weight, train_data[0][1])
  #  debug(weight)
  #  add_fv(weight, train_data[1][1])
  #  sub_fv(weight, train_data[2][1])
  #  debug(weight)
  #  debug(mult_fv(weight, train_data[2][1]))
  #  x = [1, 1, 1, 1]
  #  update_weight(x, (1, [(3, -2), (2, -2), (1, -2)]))
  #  debug(x)


if __name__ == "__main__":
  main()
