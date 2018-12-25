FROM python:3.5-alpine

ADD web /web

WORKDIR /web

RUN pip install flask redis

CMD ["python", "app.py"]
