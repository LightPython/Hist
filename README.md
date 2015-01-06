Hist
====

This write history of Python interpreter to file.

How to install.
	make
	sudo make install
or
	python setup.py build
	sudo python setup.py install

How to use. Type as below.
	import hist
	hist.hist.make("ファイル名") # ファイル名.py
or
	import hist
	hist.hist.make_rand() # X[a-zA-Z0-9_].py

