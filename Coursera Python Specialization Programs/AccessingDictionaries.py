# Dictionary declaration 

purse = dict()
purse['2000"s'] = 4
purse['500"s'] = 10
purse['100"s'] = 5

print(purse)

total = ( purse['100"s'] * 100)+ (purse['2000"s'] * 2000)+ (purse['500"s'] * 500)
print(total)

series = { 'GoT' : 9.4 , 'BB' : 9.9 , 'PB' : 8.9 , 'MH' : 9.2}
print(series)
series['GoT'] = 9.5
print(series)

# Empty Dictionaries

null = {}
print(null)

if 'GoT' in series:
    print('True')

# Program to find the most repeated word in a group of words
  # method 1
words = dict()
names = ['cwen', 'csev', 'csev', 'zwen', 'zwen', 'cwen', 'cwen']

for name in names:
    if name not in words:
        words[name] = 1
    else:
        words[name] = words[name] + 1

print(words)

  # method 2
words1 = dict()
names1 = ['cwen', 'csev', 'csev', 'zwen', 'zwen', 'cwen', 'cwen']
for name in names1:
    words1[name] = words1.get(name, 0) + 1

print(words1)

# Using for loop for dictionaries

series = { 'GoT' : 9.4 , 'BB' : 9.9 , 'PB' : 8.9 , 'MH' : 9.2}
for key in series:
    print(key, series[key])

# Retrieving lists of keys and values

print(series)
print(series.keys())
print(series.values())
print(series.items()) # Tuples

# Multi iteration varaibles 

for name,rating in series.items():
    print(name,rating)

