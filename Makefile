t: test

test:
	python -m unittest discover -p '*_test.py' -v

c: clean

clean:
	rm -f *.pyc
	rm -rf __pycache__
