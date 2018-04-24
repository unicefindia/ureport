###############################################################################
# Build stage
# Creation date: 10/01/2018
# Author: eltonplima
###############################################################################
FROM dr1:5000/ureport:base

WORKDIR /home/app
COPY . .
RUN python manage.py collectstatic --noinput
COPY supervisor.d/ureport.conf.disabled supervisor.d/ureport.conf
EXPOSE 8000
