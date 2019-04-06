FROM python:3.7-alpine
MAINTAINER Mad Software Scientist

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /server
WORKDIR /server
COPY ./server /server

RUN adduser -D edu-games
USER edu-games
