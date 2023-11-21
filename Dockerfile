FROM python:3.11.4-slim-buster
LABEL maintainer="adamchuk.oksana01.08@gmail.com"

RUN apt-get update \
    && apt-get install -y build-essential graphviz libgraphviz-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    graph-user

RUN chown -R graph-user:graph-user /vol/
RUN chmod -R 755 /vol/web/

USER graph-user
