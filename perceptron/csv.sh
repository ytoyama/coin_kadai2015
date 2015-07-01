#!/bin/sh

CSV_DIR=csv
TRAIN_DATA=train_cv0.txt
TEST_DATA=test_cv0.txt

N_TRAIN_INSTANCES=$(wc -l "$TRAIN_DATA")
N_UPDATES=$(expr $N_UPDATES \* 8)

UPDATES_CSV=updates.csv
BIAS_CSV=bias.csv
MARGIN_CSV=margin.csv


# create new files

for file in "$UPDATE_CSV" "$BIAS_CSV" "$MARGIN_CSV"
do
  : > "$file"
done


# updates

echo creating "$CSV_DIR/$UPDATE_CSV"
for num in $(seq 1 8)
do
  echo "$num,$(python3 perceptron.py -u $(expr $N_TRAIN_INSTANCES \* $num) \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$UPDATES_CSV"
done


# bias

echo creating "$CSV_DIR/$BIAS_CSV"
for num in $(seq 0 0.2 3)
do
  echo "$num,$(python3 perceptron.py -b $num -u $N_UPDATES \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$BIAS_CSV"
done


# margin

echo creating "$CSV_DIR/$MARGIN_CSV"
for num in $(seq 0 0.2 3)
do
  echo "$num,$(python3 perceptron.py -m $num -u $N_UPDATES \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$MARGIN_CSV"
done
