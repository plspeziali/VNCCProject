#!/bin/bash

docker build -t initializer ./initializer/app
docker build -t inserter ./inserter/app
docker build -t predictor ./predictor/app
docker build -t training ./training/app
docker build -t webserver ./webserver/app

kubectl delete deployment --all
kubectl delete service --all
kubectl delete pod --all

kubectl apply -f app-network-networkpolicy.yaml
kubectl apply -f db-claim1-persistentvolumeclaim.yaml
kubectl apply -f db-deployment.yaml
kubectl apply -f db-service.yaml
kubectl apply -f initializer-deployment.yaml
kubectl apply -f inserter-deployment.yaml
kubectl apply -f inserter-service.yaml
kubectl apply -f model-data-persistentvolumeclaim.yaml
kubectl apply -f pgadmin-deployment.yaml
kubectl apply -f pgadmin-service.yaml
kubectl apply -f postgres-data-persistentvolumeclaim.yaml
kubectl apply -f predictor-deployment.yaml
kubectl apply -f predictor-service.yaml
kubectl apply -f training-deployment.yaml
kubectl apply -f training-service.yaml
kubectl apply -f webserver-deployment.yaml
kubectl apply -f webserver-service.yaml

kubectl port-forward service/webserver 8080:80