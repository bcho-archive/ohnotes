.PHONY: clean-pyc clean

run_server:
	python run.py


build_db:
	python make_db.py

clean:  clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
