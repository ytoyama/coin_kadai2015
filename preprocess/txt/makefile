RM = rm -rf
POS_DATA = pos_data.txt
NEG_DATA = neg_data.txt
TRAIN_DATA = train_cv0.txt
TEST_DATA = test_cv0.txt
TARGET_FILES = ${TRAIN_DATA} ${TEST_DATA}


all: ${DATA_FILES}

${TRAIN_DATA}: ${POS_DATA} ${NEG_DATA}
	head -n 900 ${POS_DATA} > ${.TARGET}
	head -n 900 ${NEG_DATA} >> ${.TARGET}

${TEST_DATA}: ${POS_DATA} ${NEG_DATA}
	tail -n 100 ${POS_DATA} > ${.TARGET}
	tail -n 100 ${NEG_DATA} >> ${.TARGET}

clean:
	${RM} -rf ${TARGET_FILES}


.PHONY: all clean
