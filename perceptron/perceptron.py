#!/usr/bin/env python3

import sys
import math


# debugger

DEBUG = False
def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


# functions

def read_instance(line):
  return (int(line.split()[0]),
      [(int(fv_elem.split(':')[0]), int(fv_elem.split(':')[1]))
      for fv_elem in line.split()[1:]])

def read_data(filename):
  with open(filename) as f:
    instances = [read_instance(line)
        for line in f.read().split('\n') if line]
  return (instances, max(len(instance[1]) for instance in instances))

def add_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] += fv_elem[1]

def sub_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] -= fv_elem[1]

def mult_fv(wight, fv):
  assert len(weight) >= len(fv)
  return sum(x * y[1] for x, y in zip(weight, fv))

def update_weight(weight, instance):
  if mult_fv(weight, instance[1]) * instance[0] <= 0 and instance[0] > 0:
    add_fv(weight, instance[1])
  elif mult_fv(weight, instance[1]) * instance[0] <= 0 and instance[0] < 0:
    sub_fv(weight, instance[1])
  else:
    debug("weight was not updated.")

def evaluate(weight, instances):
  num_of_correct_answers = sum(mult_fv(weight, instance[1]) * instance[0] > 0
      for instance in instances)
  return (
        num_of_correct_answers,
        len(instances),
        num_of_correct_answers / len(instances)
      )


# main routine

if __name__ == "__main__":
  assert len(sys.argv) == 3, \
      "usage: {} <train data> <test data>".format(sys.argv[0])

  # process train data
  train_instances, train_max_index = read_data(sys.argv[1])
  weight = [0] * (train_max_index + 1)
  for instance in train_instances:
    update_weight(weight, instance)
  debug(weight)

  # process test data
  test_instances, test_max_index = read_data(sys.argv[2])
  print(*evaluate(weight, test_instances))

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
