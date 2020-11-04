import  json
with open("./dcard.json" , "r" , encoding="utf-8") as f:
    #read the json string
    s=f.read()

#Transform s to Dict or List

json_data=json.loads(s)
print(type(json_data))
print((json_data[1]))
