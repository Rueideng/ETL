import  json

jsondata={
    "001":{
        "Name":"Allen"
    },
    "002":{
        "Name": "Ted",
        "Interest": ["a","b","c"]
    }
}

json_str=json.dumps(jsondata)
print(json_str)
print(type(json_str))

with open("test.json","w",encoding = "utf-8") as f:
    f.write(json_str)

json_data = json.loads(json_str)
print(json_data)
print(type(json_data))