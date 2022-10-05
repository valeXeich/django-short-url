FROM python:3.11.0b5-alpine3.16

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

WORKDIR /app

COPY ./short_url /app