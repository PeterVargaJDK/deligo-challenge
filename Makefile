test:
	pytest tests


install:
	pip install -c constraints.txt .[dev]


start:
	python src/run_server.py
