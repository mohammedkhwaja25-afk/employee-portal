#!/bin/bash

set -e

echo "=================================="
echo "Starting Kubernetes Deployment..."
echo "=================================="

kubectl set image deployment/employee-portal \
employee-portal=${DOCKER_USERNAME}/employee-portal:latest

kubectl rollout status deployment/employee-portal

echo "=================================="
echo "Deployment completed successfully!"
echo "=================================="
