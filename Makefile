.PHONY: install test demo table map clean

install:
	pip install -e . && pip install pytest

test:
	pytest -q

demo:
	python examples/demo.py

table:
	stellar-relativity table --speed 0.9

map:
	stellar-relativity map

clean:
	rm -rf build dist *.egg-info .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
