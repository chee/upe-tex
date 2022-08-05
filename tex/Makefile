TEX = upe.tex preface.tex \
	ch1.tex ch2.tex ch3.tex ch4.tex ch5.tex ch6.tex ch7.tex ch8.tex ch9.tex

all: upe.html

upe.html: ${TEX}
	latex2html upe.tex
	latex2html upe.tex

clean:
	rm upe.html *.toc *.log *.aux *.out

