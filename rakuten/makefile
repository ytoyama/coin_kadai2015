RM = rm -rf
SOURCE_DATA_FILE = rakuten_reviews.txt.gz
LABEL_FILE = labels.txt
JP_TEXT_FILE = texts.txt.gz
ALL_DATA_FILES = ${LABEL_FILE} ${JP_TEXT_FILE}

all:
	@echo nothing to do

all_data: ${ALL_DATA_FILES}

${LABEL_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 8 > ${LABEL_FILE}
	python3 binarize.py ${LABEL_FILE}

${JP_TEXT_FILE}: ${SOURCE_DATA_FILE}
	zcat ${.ALLSRC} | head -n 2000 | cut -f 9 | gzip > ${JP_TEXT_FILE}

clean:
	${RM} ${ALL_DATA_FILES}


.PHONY: clean all all_data
