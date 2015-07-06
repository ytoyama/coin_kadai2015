RM = rm -rf

SOURCE_DATA_FILE = rakuten_reviews.txt.gz

LABEL_FILE = labels.txt
TEXT_FILE = texts.txt.gz
NORM_TEXT_FILE = texts_norm.txt.gz

FV_FILE = data2000.txt
TRAIN_FV_FILE = train.txt
TEST_FV_FILE = test.txt

ALL_DATA_FILES = ${LABEL_FILE} ${TEXT_FILE} ${NORM_TEXT_FILE} \
    ${FV_FILE} ${TRAIN_FV_FILE} ${TEST_FV_FILE}


all: ${ALL_DATA_FILES}

${LABEL_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 8 > ${LABEL_FILE}
	python3 binarize.py ${LABEL_FILE}

${TEXT_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 9 | gzip > ${TEXT_FILE}

${NORM_TEXT_FILE}: ${TEXT_FILE}
	python2 normalize.py ${TEXT_FILE} ${NORM_TEXT_FILE}

${FV_FILE}: ${LABEL_FILE} ${NORM_TEXT_FILE}
	python2 texts_to_fv.py ${NORM_TEXT_FILE} > MAKE_TEMP.txt
	paste -d ' ' ${LABEL_FILE} MAKE_TEMP.txt > ${FV_FILE}
	${RM} MAKE_TEMP.txt

${TRAIN_FV_FILE}: ${FV_FILE}
	head -n 1000 ${.ALLSRC} > ${.TARGET}

${TEST_FV_FILE}: ${FV_FILE}
	tail -n 1000 ${.ALLSRC} > ${.TARGET}

clean:
	${RM} ${ALL_DATA_FILES} *.db


.PHONY: clean all
