# http://10.0.2.42:999/system_check
import requests # pip install requests
import re
import datetime
import argparse
import os.path

parser = argparse.ArgumentParser(description='Enter log path and ip')
log_file = parser.add_argument("log_file", help="name of output file", type=str)
ip_server = parser.add_argument("ip_server", help="server is found data to actions", type=str)
args = parser.parse_args()
if not os.path.exists(args.log_file):
    file = open(args.log_file ,"w")
else:
    file = open(args.log_file, "a+")
url = "http://" + args.ip_server + ":999/system_check"
services = requests.get(url)
strings = re.findall('<h1 style="color:[A-Za-z ]+">[A-Za-z ]+:</h1>' ,services.text)
for string in strings:
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    micro_service = re.search('>[A-Za-z ]+:<' ,string).group(0)[1:-2]
    if "lightgreen" in string:
        file.write(str(date) + "," + micro_service + ",Online\n")
    else:
        file.write(str(date) + "," + micro_service + ",Offline\n")

# create a new repository on the command line:
# echo "# pythonProject1" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/eyal7775/pythonProject1.git
# git push -u origin main

# push an existing repository from the command line:
# git remote add origin https://github.com/eyal7775/pythonProject1.git
# git branch -M main
# git push -u origin main