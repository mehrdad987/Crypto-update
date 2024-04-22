import requests
import re
import json
#recieve
r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#decode
response=str(r.content)
x = re.findall("rate\":.*?de", response)
y=x[0]
# make it clean
z=re.findall("\d........", y)
cost=z[0]
#code
cost2={"price":cost}
bitjson=json.dumps(cost2)
