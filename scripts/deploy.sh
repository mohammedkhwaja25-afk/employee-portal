#!/bin/bash

set -e

echo "Updating Kubernetes deployment..."

kubectl set image deployment/employee-portal \
employee-portal=mohammedkhaja25/employee-portal:latest

kubectl rollout status deployment/employee-portal

echo "Deployment completed successfully!"
