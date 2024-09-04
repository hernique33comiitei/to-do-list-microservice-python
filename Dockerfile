FROM python:3.9-slim

WORKDIR /usr/app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH=/usr/app/src

COPY src/ ./src

EXPOSE 5000
