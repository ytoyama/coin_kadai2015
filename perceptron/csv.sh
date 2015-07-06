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


# configuration

## parse arguments
if [ $# -eq 2 ] && [ -f $1 ] && [ -f $2 ]
then
  TRAIN_DATA=$1
  TEST_DATA=$2
  echo "\$TRAIN_DATA = $TRAIN_DATA"
  echo "\$TEST_DATA = $TEST_DATA"
else
  echo "usage: $0 <numOfIteration> <train fv file> <test fv file>" >&2
  exit 1
fi

N_TRAIN_INSTANCES=$(echo $(wc -l "$TRAIN_DATA") | cut -f 1 -d ' ')
N_UPDATE=$(expr $N_TRAIN_INSTANCES \* 8)

## constants
CSV_DIR=csv
UPDATE_STR=update
MARGIN_STR=margin

## read configuration file
### define MARGIN_RANGE, UPDATE_RANGE, and N_ITER
N_ITER=invalid_value
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
echo "\$N_ITER = $N_ITER"

### check if all numbers in UPDATE_RANGE and MARGIN_RANGE
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
test $N_ITER -gt 0 || exit 1



# sub routines

csvFileName() {
  if [ $# -eq 2 ]
  then
    echo "${1}-${2}_$(echo "$TRAIN_DATA" | tr ' .-' '___').csv"
    return
  else
    echo "csvFileName(): invalid arguments" >&2
    exit 1
  fi
}


# main routine

for i_iter in $(seq 1 $N_ITER)
do

  # create new output files

  for file in "$UPDATE_STR" "$MARGIN_STR"
  do
    : > "$CSV_DIR/$(csvFileName "${i_iter}" "$file")"
  done


  # updates

  for num in $UPDATE_RANGE
  do
    outputFile="$CSV_DIR/$(csvFileName "${i_iter}" "$UPDATE_STR")"
    echo "$num,$(python3 perceptron.py -u \
        $(expr $N_TRAIN_INSTANCES \* $num) \
        "$TRAIN_DATA" "$TEST_DATA")" >> "$outputFile"
    echo "$outputFile updates=$num done!"
  done &
  allProcs="$allProcs $!"


  # margin
  
  for num in $MARGIN_RANGE
  do
    outputFile="$CSV_DIR/$(csvFileName "${i_iter}" "$MARGIN_STR")"
    echo "$num,$(python3 perceptron.py -m $num -u $N_UPDATE \
        "$TRAIN_DATA" "$TEST_DATA")" >> "$outputFile"
    echo "$outputFile margin=$num done!"
  done &
  allProcs="$allProcs $!"

done


wait
