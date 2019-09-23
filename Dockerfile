FROM python:3.7

ADD /src/pythontime/print.py / 

CMD ["python", "./print.py"]