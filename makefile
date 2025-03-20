all: test

test: lint
	python3 -m doctest search.py
	python3 search.py

lint:
	flake8 search.py

format:
	black --line-length=79 search.py

clean:
