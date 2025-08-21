

PYTHON=python

run:
	$(PYTHON) app.py

install:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ *.pyc *.pyo
