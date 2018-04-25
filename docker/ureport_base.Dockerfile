###############################################################################
# Build stage
# Creation date: 10/01/2018
# Author: eltonplima
###############################################################################
FROM eltonplima/sentinel_monitor

RUN apk update && apk add libpq libxml2 libxslt libmagic nodejs yarn jpeg \
alpine-sdk postgresql-dev libffi-dev libxml2-dev py-virtualenv libxslt-dev jpeg-dev redis &&\
apk add gdal geos gdal-dev --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ &&\
yarn global add coffeescript less
COPY *.txt ./
RUN pip install -r requirements.txt
RUN apk del alpine-sdk postgresql-dev libffi-dev libxml2-dev py-virtualenv libxslt-dev jpeg-dev gdal-dev
