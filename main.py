# http://10.0.2.42:999/system_check
import requests # pip install requests
import re
import datetime
import argparse
import os.path

# "C:/Users/eyal999/Desktop/logfilename.txt" "10.0.2.42"
parser = argparse.ArgumentParser(description='Enter log path and ip')
log_path = parser.add_argument("log_path", help="path for output file", type=str)
ip_server = parser.add_argument("ip_server", help="server is found data to actions", type=str)
args = parser.parse_args()
if not os.path.exists(args.log_path):
    file = open(args.log_path ,"w")
else:
    file = open(args.log_path, "a+")
url = "http://" + args.ip_server + ":999/system_check"
services = requests.get(url)
strings = re.findall('<h1 style="color:[A-Za-z ]+">[A-Za-z ]+:</h1>' ,services.text)
for string in strings:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    micro_service = re.search('>[A-Za-z ]+:<' ,string).group(0)[1:-2]
    if "lightgreen" in string:
        file.write(str(date) + "," + micro_service + ",Online")
    else:
        file.write(str(date) + "," + micro_service + ",Offline")
    file.write('\n')