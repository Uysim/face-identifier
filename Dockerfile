FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y git python-opencv 

RUN mkdir /face_recognizer

WORKDIR /face_recognizer

COPY setup.py /face_recognizer
RUN pip install .

COPY . /face_recognizer

