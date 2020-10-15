#!/usr/bin/env python2

import subprocess
import os
import sys
import requests
import time

if len(sys.argv) == 3:
    pass
else:
    sys.exit("Arguments are missing")


tfc_dir = "/home/prometheus/node_exporter/textfile_collector/"
pid = str(os.getpid())
dns_path = sys.argv[1]
dns_file = dns_path.split("/")[-1]
dns_az = dns_file.split(".")[0]
dns_type = dns_file.split(".")[1]

record = sys.argv[2]

cmd_1 = "dig @"
cmd_2 = " -u +time=1 +tries=1 +noall +answer +stats | grep \"Query time\" | grep -oEe \"[0-9]+\""

# Get the DNS servers to be queried
with open(dns_path) as file:
    data = file.read()
    dns_list = data.split("\n")

def get_response():
    for dns in dns_list:
        if dns != "":
            f_cmd = cmd_1 + dns + " " + record + cmd_2
            try:
                query_res = subprocess.check_output(['bash', '-c', f_cmd])
            except:
                query_res = 0
        #result = "dns_query_time{type=\"" + str(dns_type) + "\",az=\"" + str(dns_az) + "\",server=\"" + dns  + "\"}" + str(query_res)
        #result_list.append(result.rstrip("\n"))

            # Prepare the payload
            job_name = "dns_response_time"
            payload_key = "dns_response_time"
            response = requests.post('http://localhost:9091/metrics/job/{j}/instance/{i}/type/{t}/az/{a}'.format(j=job_name, i=dns, t=dns_type, a=dns_az), data='{k} {v}\n'.format(k=payload_key, v=query_res))
            print(response.status_code)

get_response()
