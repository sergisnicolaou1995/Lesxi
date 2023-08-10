# Dockerfile

# pull the official docker image
FROM python:3.9-slim AS base

RUN apt-get update && apt-get install build-essential -y
# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

FROM base AS final

# copy project
COPY . /app
