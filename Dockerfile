FROM python:3.7.0-alpine3.7

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev --update bash && rm -rf /var/cache/apk/*

ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project
RUN pip install -r requirements.txt
ADD . /project/

