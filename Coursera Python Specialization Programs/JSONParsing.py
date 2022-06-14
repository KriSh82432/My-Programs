# JSON as a dictionary
import json

data = '''
{
    "name" : "Krishna.V",
    "phone" : {
        "code" : "+91",
        "number" : "7904148922"
    },
    "city" : {
        "cname" : "Salem"
    }
}
'''

info = json.loads(data)
print('Name  :',info["name"])
print('Mobile:',info["phone"]["code"],info["phone"]["number"])
print('City  :',info["city"]["cname"])

# JSON as a list

data1 = '''
[
    {
        "name" : "Krishna V",
        "user id" : "RA2111043010028",
        "rank" : 1
    },
    {
        "name": "Sidharth",
        "user id" : "RA2111043010014",
        "rank" : "0"
    }
]'''

stuff = json.loads(data1)
print('No. of Users :',len(stuff))

for item in stuff:
    print('Name :',item["name"])
    print('User ID :',item["user id"])
    print('Rank :',item["rank"])

