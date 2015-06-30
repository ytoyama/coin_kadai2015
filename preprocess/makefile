RM = rm -rf
CREATE_DATA = python2 dir_to_data.py
POS_DIR = txt_sentoken/pos
NEG_DIR = txt_sentoken/neg
POS_DATA = txt/pos_data.txt
NEG_DATA = txt/neg_data.txt
ALL_DATA_FILES = ${POS_DATA} ${NEG_DATA} train_and_test_data


all: ${ALL_DATA_FILES}

${POS_DATA}:
	${CREATE_DATA} 1 ${POS_DIR} > ${.TARGET}

${NEG_DATA}:
	${CREATE_DATA} -1 ${NEG_DIR} > ${.TARGET}

train_and_test_data: ${POS_DATA} ${NEG_DATA}
	make -C txt

clean:
	$(RM) *.db *.pyc


.PHONY: all clean train_and_test_data
