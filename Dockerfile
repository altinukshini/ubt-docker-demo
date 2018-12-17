FROM python:3.5-alpine

ADD web /web

WORKDIR /web

RUN pip install flask

CMD ["python", "app.py"]
