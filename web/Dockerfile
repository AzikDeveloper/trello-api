FROM python:3.7-slim

WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
