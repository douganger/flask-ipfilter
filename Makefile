clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	rm -rf docs/_build/* 
	rm -rf .env

distribution:
	python setup.py sdist bdist_wheel

documentation:
	python -m sphinx -M html "docs" "docs/_build"

lint: pep8 pep257 pylint

pep8:
	pycodestyle flask_ipfilter/*.py
	pycodestyle test/*.py

pep257:
	pydocstyle flask_ipfilter/*.py
	pydocstyle test/*.py

pylint:
	pylint flask_ipfilter/*.py
	pylint test/*.py

unittest:
	py.test test --disable-pytest-warnings --cov=flask_ipfilter 

