#!/bin/bash

docker-compose build --pull ureport_base &&
docker-compose build --pull ureport &&
docker-compose push ureport_base ureport
