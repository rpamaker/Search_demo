#!/bin/bash
set -e

export DOCKERHUB_REPO=danielaron/demo-rpamaker
export BUILD_VERSION=1

docker build -t $DOCKERHUB_REPO:$BUILD_VERSION .
docker push $DOCKERHUB_REPO:$BUILD_VERSION