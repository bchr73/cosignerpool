#!/bin/sh

while [ ! -f /etc/certs/fullchain.pem ]
do
	echo "sleeping"
	sleep 5
done

echo starting $NGINX_HOST
/bin/bash -c "envsubst < /etc/nginx/conf.d/CosignerpoolSSL.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
