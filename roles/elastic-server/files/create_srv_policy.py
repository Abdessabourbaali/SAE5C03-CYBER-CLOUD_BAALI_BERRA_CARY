#!/bin/python3
import requests
import sys
import json
headers={"Content-Type":"application/json",
        "Accept":"*/*",
        "Authorization":f"ApiKey {sys.argv[2]}",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "kbn-xsrf":"xxx"}
data='{"name": "GOAD-SRV"}'
auth=("elastic",sys.argv[1])
r=requests.post(f"https://{sys.argv[3]}:9200/_security/api_key?pretty",auth=auth,headers=headers,data=data,verify=False)
print(json.loads(r.content.decode())["encoded"])
