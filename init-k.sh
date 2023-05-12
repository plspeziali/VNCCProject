#!/bin/bash

docker build -t initializer ./initializer/app
docker build -t inserter ./inserter/app
docker build -t predictor ./predictor/app
docker build -t training ./training/app
docker build -t webserver ./webserver/app

kubectl delete deployment --all
kubectl delete service --all
kubectl delete pod --all

kubectl create configmap body-performance-configmap --from-file=db/bodyPerformance.csv

kubectl apply -f app-network-networkpolicy.yaml
kubectl apply -f db/db-deployment.yaml
kubectl apply -f db/db-service.yaml
kubectl apply -f initializer/initializer-deployment.yaml
kubectl apply -f inserter/inserter-deployment.yaml
kubectl apply -f inserter/inserter-service.yaml
kubectl apply -f model-data-persistentvolumeclaim.yaml
kubectl apply -f db/pgadmin-deployment.yaml
kubectl apply -f db/pgadmin-service.yaml
kubectl apply -f db/postgres-data-persistentvolumeclaim.yaml
kubectl apply -f predictor/predictor-deployment.yaml
kubectl apply -f predictor/predictor-service.yaml
kubectl apply -f training/training-deployment.yaml
kubectl apply -f training/training-service.yaml
kubectl apply -f webserver/webserver-deployment.yaml
kubectl apply -f webserver/webserver-service.yaml

sleep 60

kubectl port-forward service/webserver 80:8080