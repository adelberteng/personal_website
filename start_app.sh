rm ./nginx_conf/nginx.conf
cp ./nginx_conf/nginx_base.conf ./nginx_conf/nginx.conf
docker-compose -f ./docker/docker-compose.yaml up -d
docker exec -it nginx bash -c 'apt-get update && apt-get install certbot -y && apt-get install python3-certbot-nginx -y'
docker exec -it nginx bash -c 'nginx -t && nginx -s reload'
docker exec -it nginx bash -c 'certbot --nginx -d albertteng.xyz -d www.albertteng.xyz'