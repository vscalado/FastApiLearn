FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y
RUN apt-get install curl -y 
RUN curl -sSL https://install.python-poetry.org | python3 - 
RUN poetry config virtualenvs.create false 
RUN poetry install 
RUN apt-get remove curl -y

COPY ./app /app
WORKDIR /app

