RM = rm -rf


all: img

img:
	test -d ${.TARGET} || mkdir ${.TARGET}
	python2 conv_csv.py . img

clean:
	${RM} img/*.png


.PHONY: all clean img
