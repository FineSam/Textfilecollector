#!/usr/bin/env python2

import subprocess
import os

tfc_dir = "/home/prometheus/node_exporter/textfile_collector/"
pid = str(os.getpid())

cmd_1 = "dig @"
cmd_2 = " google.com"
cmd_3 = " +time=1 +tries=1 +noall +answer +stats | grep \"Query time\" | grep -oEe \"[0-9]+\""

# Get the DNS servers to be queried
with open("/home/centos/dns.list") as file:
    data = file.read()
    dns_list = data.split("\n")

result_list = []
for dns in dns_list:
    if dns != "":
        f_cmd = cmd_1 + dns + cmd_2 + cmd_3
	try:
            query_res = subprocess.check_output(['bash', '-c', f_cmd])
	except:
	    query_res = 0
        result = "dns_query_time{server=\"" + dns  + "\"}" + str(query_res)
        result_list.append(result.rstrip("\n"))

# Write to file
tmp_filepath = os.path.join(tfc_dir + "dns_probe.prom." + pid)
with open( tmp_filepath, 'w') as f:
    for item in result_list:
        f.write("%s\n" % item)

# Rename the temporary file atomically.
filepath = os.path.join(tfc_dir + "dns_probe.prom")
os.rename(tmp_filepath, filepath)




