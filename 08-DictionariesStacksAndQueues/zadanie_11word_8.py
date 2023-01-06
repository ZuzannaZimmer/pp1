import json

with open("data.json") as file:
    data = json.load(file)

x=0
while x<len(data):
    # print(data[x])
    for key,value in data[x].items():
        print(key,':',value)
    x=x+1

# for i in data:
#     for k,v in i.items():
#         print(k,v)