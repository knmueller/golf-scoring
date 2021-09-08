#!/bin/bash
current=""
while true; do
	latest=`ec2metadata --public-ipv4`
	echo "public-ipv4=$latest" > ~/duckdns/duck-run.log
	if [ "$current" == "$latest" ]
	then
		echo "ip not changed" >> ~/duckdns/duck-run.log
	else
		echo "ip has changed - updating" >> ~/duckdns/duck-run.log
		current=$latest
		echo url="https://www.duckdns.org/update?domains=motocana&token=55bdc529-3ae9-4d66-a776-e1931ade2fd3&ip=" | curl -k -s -o ~/duckdns/duck.log -K -
	fi
        echo "" >> ~/duckdns/duck.log
        cat ~/duckdns/duck-run.log >> ~/duckdns/duck.log
	sleep 60m
done
