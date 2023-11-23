FROM python:3.9-alpine3.16

WORKDIR /book_management

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /book_management
COPY ./requirements.txt /book_management/requirements.txt
COPY ./.env /book_management/.env

EXPOSE 8000

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
