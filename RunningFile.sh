#!/bin/bash
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
docker rmi $(docker image ls -aq)
docker build -t finvizbot:v1 .
docker start --name bot -i finvizbot
