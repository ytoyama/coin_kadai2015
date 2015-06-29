#!/usr/bin/env python3

import sys


# debugger

DEBUG = True
def debug(*x):
  if DEBUG:
    print(*x, file=sys.stderr)


# functions

def read_instance(line):
  return (line.split()[0],
      [(int(fv_elem.split(':')[0]), int(fv_elem.split(':')[1]))
      for fv_elem in line.split()[1:]])

def read_data(filename):
  with open(filename) as f:
    instance_list = [read_instance(line)
        for line in f.read().split('\n') if line]
    return (instance_list,
        max(*[len(instance[1]) for instance in instance_list]))

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


# main routine

if __name__ == "__main__":
  assert len(sys.argv) == 2
  train_data, max_index = read_data(sys.argv[1])
  #debug(train_data, max_index)
  weight = [0] * (max_index + 1)

  print(train_data[0][1])
  add_fv(weight, train_data[0][1])
  print(weight)
  add_fv(weight, train_data[1][1])
  sub_fv(weight, train_data[2][1])
  print(weight)
  print(mult_fv(weight, train_data[2][1]))
