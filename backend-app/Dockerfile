FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ADD requirements.txt /app
RUN apt-get update -y \
    && apt-get install -y libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ./app /app
