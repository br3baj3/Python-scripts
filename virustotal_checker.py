#This script is intended to check a list of several "suspicious" IPs detected in a network traffic capture. 
#Since the IP report from virustotal is limited to 4 requests for minute, a time sleep must be introuduced.
#Ouput is formated in tables for an html file.

import json
import urllib
import sys
import os
import time
from json2html import *

counter=0
url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'

IPlist=open("list_IPs.txt")
IPreput=open("Reputation_IPs.html","w")
IP=IPlist.readline().rstrip('\n')

while IP!="":
    counter=counter+1
    mod=counter%4
    if mod==0:
        time.sleep(60)
        counter=0

    parameters = {'ip': IP, 'apikey': 'YOUR_VIRUS_TOTAL_API_KEY'}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    response_dict2=json2html.convert(json = response_dict)
    IPreput.write(str(response_dict2))
    IP=IPlist.readline().rstrip('\n')

IPlist.close()
IPreput.close()         
