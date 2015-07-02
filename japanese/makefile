RM = rm -rf
DIC_FILE = mecab.dic
CSV_DIC_FILE = mecab.csv
DIC_ENCODING = utf-8

all:
	@echo nothing to make

${DIC_FILE}: ${CSV_DIC_FILE}
	/usr/local/libexec/mecab/mecab-dict-index -d/usr/local/lib/mecab/dic/ipadic \
			-u ${DIC_FILE} -f ${DIC_ENCODING} -t ${DIC_ENCODING} ${CSV_DIC_FILE}

clean:
	${RM} ${DIC_FILE}


.PHONY: clean all
