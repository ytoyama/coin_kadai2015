#!/bin/sh

LIBLINEAR_DIR='../liblinear*'

TRAIN_FILE='train_cv0.txt'
TEST_FILE='test_cv0.txt'

if [ $# -eq 0 ]
then
  echo "usage: $0 <number>..." >&2
  exit 1
fi

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
