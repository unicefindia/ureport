FROM dr1:5000/ureport:base

WORKDIR /home/app
COPY . .
COPY supervisor.d/celery.conf.disabled supervisor.d/celery.conf
EXPOSE 8000
