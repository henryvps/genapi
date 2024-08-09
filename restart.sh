#/bin/sh
docker rm -f `docker ps -aq`
docker container prune
docker image prune
docker compose build --no-cache
docker compose up -d