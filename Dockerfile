FROM python:3.11-slim

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY CSVData/ CSVData/
COPY DataLoaderModule/ DataLoaderModule/
COPY FixedVariables/ FixedVariables/
COPY FlaskModule/ FlaskModule/
COPY LoguruModule/ LoguruModule/
COPY PostgresDBModule/ PostgresDBModule/
COPY SQLScripts/ SQLScripts/
COPY templates/ templates/
COPY .env .env
COPY .env.docker .env.docker
COPY app.py app.py
