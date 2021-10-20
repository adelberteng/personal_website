FROM python:3.9-slim
LABEL MAINTAINER="AlbertTeng"
LABEL NAME="personal website"
LABEL Version="0.1.1"

USER root
COPY ./requirements.txt /requirements.txt
WORKDIR /personal_website
EXPOSE 5000/tcp
RUN apt update && pip3 install -r /requirements.txt --no-cache-dir
CMD gunicorn -c /personal_website/conf/gunicorn_config.py --chdir ./src wsgi:app