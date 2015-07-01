PYTHON = python3
PYTHON_PROG = perceptron.py
TRAIN_FILE = train_cv0.txt
TEST_FILE = test_cv0.txt


all:
	@echo nothing to do

test_options:
	@echo "# no option"
	${PYTHON} ${PYTHON_PROG} ${TRAIN_FILE} ${TEST_FILE} 
	@echo "# invalid options"
	${PYTHON} ${PYTHON_PROG} -a invalid_arg ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -b ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -m ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -n invalid_arg ${TRAIN_FILE} ${TEST_FILE} || true
	${PYTHON} ${PYTHON_PROG} -u ${TRAIN_FILE} ${TEST_FILE} || true
	@echo "# valid options"
	@echo "## perceptron not averaged"
	${PYTHON} ${PYTHON_PROG} -a ${TRAIN_FILE} ${TEST_FILE} 
	@echo "## bias"
	${PYTHON} ${PYTHON_PROG} -b 0 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 0.25 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 0.5 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 0.75 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 1 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 1.5 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -b 2 ${TRAIN_FILE} ${TEST_FILE} 
	@echo "## margin"
	${PYTHON} ${PYTHON_PROG} -m 0 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -m 0.1 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -m 0.25 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -m 0.5 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -m 0.75 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -m 1 ${TRAIN_FILE} ${TEST_FILE} 
	@echo "## not normarized feature vectors"
	${PYTHON} ${PYTHON_PROG} -n ${TRAIN_FILE} ${TEST_FILE} 
	@echo "## limited max num of updates"
	${PYTHON} ${PYTHON_PROG} -u 1 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -u 50 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -u 100 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -u 200 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -u 500 ${TRAIN_FILE} ${TEST_FILE} 
	${PYTHON} ${PYTHON_PROG} -u 1000 ${TRAIN_FILE} ${TEST_FILE} 

.PHONY: test
