# http://10.0.2.42:999/system_check
import requests # pip install requests
import re
import datetime
import argparse

parser = argparse.ArgumentParser(description='Enter log path and ip')
log_file = parser.add_argument('-f', '--file', help="name of output file", type=str, required=True)
ip_server = parser.add_argument('-e', '--env', help="server is found data to actions", type=str, required=True)
args = vars(parser.parse_args())
with open(args['file'], "a+") as file:
    url = "http://" + args['env'] + ":999/system_check"
    services = requests.get(url)
    strings = re.findall('<h1 style="color:[A-Za-z ]+">[A-Za-z ]+:</h1>' ,services.text)
    for string in strings:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        micro_service = re.search('>[A-Za-z ]+:<' ,string).group(0)[1:-2]
        if "lightgreen" in string:
            file.write(str(date) + "," + micro_service + ",Online\n")
        else:
            file.write(str(date) + "," + micro_service + ",Offline\n")
    file.write("---\n")