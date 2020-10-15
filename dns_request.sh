#!/bin/sh
while ((1)) ; do
    python /home/prometheus/pushgateway/dnsrequesttime.py /home/prometheus/pushgateway/eu.global.list google.com
    python /home/prometheus/pushgateway/dnsrequesttime.py /home/prometheus/pushgateway/jp.global.list google.com
    sleep 1
done
