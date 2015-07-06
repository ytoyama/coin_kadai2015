#!/bin/sh

LIBLINEAR_DIR='./liblinear*'

if [ $# -lt 3 ]
then
  echo "usage: $0 <train file> <test file> <number>..." >&2
  exit 1
fi

TRAIN_FILE=$1
TEST_FILE=$2
shift 2

for cost_index in "$@"
do
  MODEL_FILE="${TRAIN_FILE}_${cost_index}.model"
  echo "cost = ${cost_index}: training finished!" \
      $(${LIBLINEAR_DIR}/train -s 0 -B 1 \
          -c $(python -c "print(2 ** $cost_index)") \
          "$TRAIN_FILE" "$MODEL_FILE" > /dev/null \
      && ${LIBLINEAR_DIR}/predict -b 1 "$TEST_FILE" "$MODEL_FILE" /dev/null \
          | tail -n 1 | tee "c_${cost_index}.log") &
done

wait
echo 'all process finished!'
