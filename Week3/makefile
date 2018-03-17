PYTHON = python
VIEWER = less

.PHONY: clean run view

problem1 :  problem1.py
	$(PYTHON) problem1.py $(arg)

problem2 :  problem2.py
	$(PYTHON) problem2.py $(arg)

problem3 :  problem3.py
	$(PYTHON) problem3.py
	gnuplot < plot-instructions
	open plot.png

view:
	$(VIEWER) problem1.py problem2.py

clean:
	rm *.pyc yoan.out plot.png

run: problem1 problem2 problem3 view
