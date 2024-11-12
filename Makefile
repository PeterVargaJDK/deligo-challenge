test:
	pytest tests


install:
	pip install -c constraints.txt .[dev]


start:
	python src/run_server.py

load-test:
	locust -f src/simulate_kiosks.py -H http://localhost:8000 Kiosk -u 250 -t 180s -r 10
