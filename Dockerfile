FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y git python-opencv 

RUN mkdir /face_recognizer

WORKDIR /face_recognizer

COPY requirements.txt /face_recognizer
RUN pip install -r requirements.txt

COPY . /face_recognizer
