FROM python:2.7-slim-buster

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY covid19_webservice /srv/covid19_webservice
WORKDIR /srv/


CMD ["python", "-um", "covid19_webservice"]
