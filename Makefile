install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=my_lib test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py