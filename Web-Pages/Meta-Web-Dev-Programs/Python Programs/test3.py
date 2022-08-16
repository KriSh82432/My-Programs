a = [[96, 45],[69]]
print("".join(list(map(str, a))))

list = ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management',
        'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']

new = [x.replace("_", " ") for x in list]
print(new)

employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

index = 0
new = {}
for i in employee_list:
  new[employee_list[index]['name'][0]] = employee_list[index]['id']
  index += 1

print(new)

newl = ["pizza", "pasta", "falafel"]
name = str()

for x in newl:
  name = name + x + " "

print(name)