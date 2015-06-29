#!/usr/bin/env python3

import sys
import math


# debugger

DEBUG = True
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
    instance_list = [read_instance(line)
        for line in f.read().split('\n') if line]
  return (instance_list, max(len(instance[1]) for instance in instance_list))

def add_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] += fv_elem[1]

def sub_fv(weight, fv):
  assert len(weight) >= len(fv)
  for fv_elem in fv:
    weight[fv_elem[0]] -= fv_elem[1]

def mult_fv(wight, fv):
  if len(fv) > len(weight):
    return False
  assert len(weight) >= len(fv)
  return sum(x * y[1] for x, y in zip(weight, fv))

def update_weight(weight, instance):
  if mult_fv(weight, instance[1]) * instance[0] < 0 and instance[0] > 0:
    add_fv(weight, instance[1])
  elif mult_fv(weight, instance[1]) * instance[0] < 0 and instance[0] < 0:
    sub_fv(weight, instance[1])
  else:
    raise RuntimeError("maybe invalid label: {}".format(instance[0]))


# main routine

if __name__ == "__main__":
  assert len(sys.argv) == 3, \
      "usage: {} <train data> <test data>".format(sys.argv[0])
  train_data, max_index = read_data(sys.argv[1])
  test_data, test_max_index = read_data(sys.argv[2])
  #debug(train_data, max_index)
  weight = [0] * (max_index + 1)

  print(train_data[0])
  add_fv(weight, train_data[0][1])
  print(weight)
  add_fv(weight, train_data[1][1])
  sub_fv(weight, train_data[2][1])
  print(weight)
  print(mult_fv(weight, train_data[2][1]))
  x = [1, 1, 1, 1]
  update_weight(x, (1, [(3, -2), (2, -2), (1, -2)]))
  print(x)
