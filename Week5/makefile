
# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run prob1 view

# run will call your test_post target, below
run : prob1 view
# if you also submit a file called sample-post.input, then this target
# will be run automatically by the submit wrapper, so you can see it
# working
prob1: prob1.py
	python3 prob1.py

view: 
	less prob1.py

clean:
	rm *.pyc
	rm *.txt
