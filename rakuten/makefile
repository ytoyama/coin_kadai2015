RM = rm -rf
SOURCE_DATA_FILE = rakuten_reviews.txt.gz
LABEL_FILE = labels.txt
JP_TEXT_FILE = texts.txt.gz
NORM_JP_TEXT_FILE = texts_norm.txt.gz
ALL_DATA_FILES = ${LABEL_FILE} ${JP_TEXT_FILE} ${NORM_JP_TEXT_FILE}


all: ${ALL_DATA_FILES}

${LABEL_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 8 > ${LABEL_FILE}
	python3 binarize.py ${LABEL_FILE}

${JP_TEXT_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 9 | gzip > ${JP_TEXT_FILE}

${NORM_JP_TEXT_FILE}: ${JP_TEXT_FILE}
	python2 normalize.py ${JP_TEXT_FILE} ${NORM_JP_TEXT_FILE}

clean:
	${RM} ${ALL_DATA_FILES} *.db


.PHONY: clean all
