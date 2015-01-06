# Hist

This write a history of Python interpreter to file.

## How to install.
Type as below on shell or bash interpreter etc:

	python setup.py build
	sudo python setup.py install

## How to use.
If you want to write a history of python interpreter to file,
type as below on python interpreter after written a program of interpreter:

	import hist
	hist.hist.make("filename")

and, when you want to create random's filename, Type as below on python interpreter:

	import hist
	hist.hist.make_rand() # X[a-zA-Z0-9_].py

