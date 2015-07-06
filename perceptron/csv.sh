#!/bin/sh

TRAPPED_SIGNAL="1 2 3 15"

trap "
  for pid in \$allProcs
  do
    kill -0 \$pid > /dev/null 2>&1 && kill \$pid
  done
  echo \"killed!\" >&2
  exit 1
" $TRAPPED_SIGNAL
allProcs=


CSV_DIR=csv
TRAIN_DATA=train_cv0.txt
TEST_DATA=test_cv0.txt

N_TRAIN_INSTANCES=$(echo $(wc -l "$TRAIN_DATA") | cut -f 1 -d ' ')
N_UPDATE=$(expr $N_TRAIN_INSTANCES \* 8)

UPDATE_CSV=updates.csv
MARGIN_CSV=margin.csv

# define MARGIN_RANGE and UPDATE_RANGE
UPDATE_RANGE=invalid_value
MARGIN_RANGE=invalid_value
if [ -f ./config.sh ]
then
  . ./config.sh
else
  exit 1
fi
echo "\$UPDATE_RANGE = $(echo $UPDATE_RANGE)"
echo "\$MARGIN_RANGE = $(echo $MARGIN_RANGE)"

## check if all numbers in UPDATE_RANGE and MARGIN_RANGE
for num in $UPDATE_RANGE
do
  # every num must be a integer
  expr $num \* 1 > /dev/null || exit 1
done
for num in $MARGIN_RANGE
do
  # every num must be equal to or greater than 0
  expr $num \>= 0 > /dev/null || exit 1
done


# parse arguments

if [ $# == 1 ] && [ $1 -gt 0 ]
then
  echo num of iteration = $1
  numOfIter=$1
else
  echo "usage: $0 <numOfIteration>" >&2
  exit 1
fi


# main routine

for i_iter in $(seq 1 $numOfIter)
do

  # create new files

  for file in "$UPDATE_CSV" "$MARGIN_CSV"
  do
    : > "$CSV_DIR/${i_iter}_$file"
  done


  # updates

  for num in $UPDATE_RANGE
  do
    outputFile="$CSV_DIR/${i_iter}_$UPDATE_CSV"
    echo "$num,$(python3 perceptron.py -u \
        $(expr $N_TRAIN_INSTANCES \* $num) \
        "$TRAIN_DATA" "$TEST_DATA")" >> "$outputFile"
    echo "$outputFile updates=$num done!"
  done &
  allProcs="$allProcs $!"


  # margin
  
  for num in $MARGIN_RANGE
  do
    outputFile="$CSV_DIR/${i_iter}_$MARGIN_CSV"
    echo "$num,$(python3 perceptron.py -m $num -u $N_UPDATE \
        "$TRAIN_DATA" "$TEST_DATA")" >> "$outputFile"
    echo "$outputFile margin=$num done!"
  done &
  allProcs="$allProcs $!"

done


wait
