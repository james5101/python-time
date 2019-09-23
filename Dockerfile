FROM python:3.7

ADD /src/python.py / 

CMD ["python", "./python.py"]