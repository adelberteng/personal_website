#!/bin/bash
_TOP_DIR_PATH=$(cd "$(dirname "$0")"; cd ..;pwd)
# python3 ./src/secret_to_config.py
# rm $_TOP_DIR_PATH/nginx_conf/nginx.conf
# cp $_TOP_DIR_PATH/nginx_conf/nginx_base.conf $_TOP_DIR_PATH/nginx_conf/nginx.conf
docker-compose -f $_TOP_DIR_PATH/docker/docker-compose.yaml up -d
# docker exec -it nginx bash -c 'apt-get update && apt-get install certbot -y && apt-get install python3-certbot-nginx -y'
# docker exec -it nginx bash -c 'nginx -t && nginx -s reload'
# docker exec -it nginx bash -c 'certbot --nginx --email adelberteng@gmail.com --agree-tos --no-eff-email -d albertteng.xyz -d www.albertteng.xyz'