import requests
import json
data = requests.get("https://api.irail.be/v1/vehicle/?id=BE.NMBS.IC1832&format=json&lang=en&alerts=false")
json_obj = json.loads(data.text)

print(json_obj)

json_file = open("json_dump.txt","w")

json_file.write(json.dumps(json_obj))
