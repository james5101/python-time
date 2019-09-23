run:
	python python.py

test:
	pytest

docker-build:
	docker build -t python-time .

docker-run:
	docker run python-time