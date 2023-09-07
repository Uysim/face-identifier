FROM python:3.11-slim-buster

RUN mkdir /face_recognizer

WORKDIR /face_recognizer

COPY requirements.txt /face_recognizer
RUN pip install -r requirements.txt
COPY . /face_recognizer
