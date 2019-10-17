#!/bin/sh

if [ ! -f /etc/certs/fullchain.pem ]
then
	echo "no certs found, generating"
	openssl req -subj '/C=US/ST=Florida/L=Fort Lauderdale/O=Fluid Chains Inc./OU=Fluid Chains Inc./CN=cosigner.exos.to' -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out /etc/certs/fullchain.pem -keyout /etc/certs/privkey.pem
else
	echo "found certs, attempting renewal"
	exit 0
fi
