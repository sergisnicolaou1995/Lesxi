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
COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

# copy project
COPY . /app

CMD gunicorn --capture-output --error-logfile ./logs.txt --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker main:app --timeout 60