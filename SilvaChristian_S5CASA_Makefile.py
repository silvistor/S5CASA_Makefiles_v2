all: resultados.pdf

datos.dat:
	python makedatos.py > datos.dat

makedatos1:
	g++ makedatos1.cpp -o makedatos1

datos1.dat: makedatos1
	./makedatos1 > datos1.dat

graficas: datos.dat datos1.dat
	python plotdatos.py
	python plotdatos1.py

resultados.pdf: graficas resultados.tex
	pdflatex resultados.tex

clean:
	rm -f *.aux *.log *.out makedatos1 resultados.pdf datos.dat datos1.dat