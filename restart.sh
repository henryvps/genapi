#/bin/sh
docker rm -f `docker ps -aq`
docker container prune -f
docker image prune -f
docker compose build --no-cache
docker compose up -d