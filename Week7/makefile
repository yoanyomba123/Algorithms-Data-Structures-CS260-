
# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run 

# run will call your test_post target, below
run : test-set prob2 
# if you also submit a file called sample-post.input, then this target
# will be run automatically by the submit wrapper, so you can see it
# working
test-set: test-set.py
	python test-set.py

prob2: prob2.py
	python prob2.py

prob2-view: 
	less prob2.py

clean:
	rm *.pyc
	rm *.txt
