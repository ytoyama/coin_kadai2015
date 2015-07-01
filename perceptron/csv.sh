#!/bin/sh

CSV_DIR=csv
TRAIN_DATA=train_cv0.txt
TEST_DATA=test_cv0.txt

N_TRAIN_INSTANCES=$(echo $(wc -l "$TRAIN_DATA") | cut -f 1 -d ' ')
N_UPDATE=$(expr $N_TRAIN_INSTANCES \* 8)

UPDATE_CSV=updates.csv
BIAS_CSV=bias.csv
MARGIN_CSV=margin.csv


# create new files

for file in "$UPDATE_CSV" "$BIAS_CSV" "$MARGIN_CSV"
do
  : > "$CSV_DIR/$file"
done


# updates

echo creating "$CSV_DIR/$UPDATE_CSV"
range=$(seq 1 8)
echo "range =" $range
for num in $range
do
  echo "i = $num"
  echo "$num,$(python3 perceptron.py -u $(expr $N_TRAIN_INSTANCES \* $num) \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$UPDATE_CSV"
done


# bias

echo creating "$CSV_DIR/$BIAS_CSV"
range=$(seq 0 0.2 3)
echo "range =" $range
for num in $range
do
  echo "i = $num"
  echo "$num,$(python3 perceptron.py -b $num -u $N_UPDATE \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$BIAS_CSV"
done


# margin

echo creating "$CSV_DIR/$MARGIN_CSV"
range=$(seq 0 0.2 3)
echo "range =" $range
for num in $range
do
  echo "i = $num"
  echo "$num,$(python3 perceptron.py -m $num -u $N_UPDATE \
      "$TRAIN_DATA" "$TEST_DATA")" >> "$CSV_DIR/$MARGIN_CSV"
done
