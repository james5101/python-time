run:
	python python.py

docker-build:
	docker build -t python-time .

docker-run:
	docker run python-time