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