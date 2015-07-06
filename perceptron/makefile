RM = rm -rf

PYTHON = python3
PYTHON_PROG = perceptron.py

.ifdef RAKUTEN
TRAIN_FILE = rakuten_train.txt
TEST_FILE = rakuten_test.txt
.else
TRAIN_FILE = train_cv0.txt
TEST_FILE = test_cv0.txt
.endif

CSV_DIR = csv
N_ITER = 8



all: csv csv/img

# touch data files when reproduce csv dir cause it's a dir
csv: ${TRAIN_FILE} ${TEST_FILE}
	@echo "# generating csv data"
	sh csv.sh ${N_ITER} ${TRAIN_FILE} ${TEST_FILE}

csv/img: csv
	make -C ${CSV_DIR}

clean:
	${RM} ${CSV_DIR}/*.csv
	make -C ${CSV_DIR} clean

test:
	@echo "# no option"
	${PYTHON} ${PYTHON_PROG} ${TRAIN_FILE} ${TEST_FILE}
	@echo "# invalid options"
	${PYTHON} ${PYTHON_PROG} -a invalid_arg ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -b invalid_arg ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -m ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -n invalid_arg ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -u ${TRAIN_FILE} ${TEST_FILE} || true
	@echo "# valid options"
	@echo "## perceptron not averaged"
	${PYTHON} ${PYTHON_PROG} -a ${TRAIN_FILE} ${TEST_FILE}
	@echo "## bias"
	${PYTHON} ${PYTHON_PROG} -b ${TRAIN_FILE} ${TEST_FILE}
	@echo "## margin"
	${PYTHON} ${PYTHON_PROG} -m 0 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -m 0.1 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -m 0.25 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -m 0.5 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -m 0.75 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -m 1 ${TRAIN_FILE} ${TEST_FILE}
	@echo "## not normarized feature vectors"
	${PYTHON} ${PYTHON_PROG} -n ${TRAIN_FILE} ${TEST_FILE}
	@echo "## num of updates"
	${PYTHON} ${PYTHON_PROG} -u 1 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 50 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 100 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 200 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 500 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 1000 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 1400 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 1800 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 2000 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 3000 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 5000 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 7500 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 10000 ${TRAIN_FILE} ${TEST_FILE}
	${PYTHON} ${PYTHON_PROG} -u 15000 ${TRAIN_FILE} ${TEST_FILE}


.PHONY: all clean test
