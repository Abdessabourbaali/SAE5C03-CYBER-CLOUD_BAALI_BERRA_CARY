#!/bin/python3
import json
import requests
import sys

headers={"Content-Type":"application/json"}
data='{"name":"cute-api-key","expiration":"7d"}'
auth=("elastic",sys.argv[1])
r=requests.post(f"https://{sys.argv[2]}:9200/_security/api_key?pretty",auth=auth,headers=headers,data=data,verify=False)
print(json.loads(r.content.decode())["encoded"])
