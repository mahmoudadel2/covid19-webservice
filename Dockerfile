FROM python:2.7-slim-buster

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY covid19_webservice /srv/covid19_webservice
WORKDIR /srv/

EXPOSE 8080

ENTRYPOINT python -um covid19_webservice
