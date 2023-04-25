#!/bin/bash

docker build -t initializer ./initializer/app
docker build -t inserter ./inserter/app
docker build -t predictor ./predictor/app
docker build -t training ./training/app
docker build -t webserver ./webserver/app

docker-compose up -d