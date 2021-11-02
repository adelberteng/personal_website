#!/bin/bash
sudo certbot certonly --webroot --webroot-path=$HOME/cert/ \
	--email adelberteng@gmail.com --agree-tos --no-eff-email \	
	--staging -d albertteng.xyz -d www.albertteng.xyz