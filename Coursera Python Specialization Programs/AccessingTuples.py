
def pause():
    pauseProgram = input('Press any key to close...')

# Tuples are modified version of Lists except tuples are unchangable

# Lists ( use square brackets)
name = ['Krishna', 'Elan', 'Gokul']
print(name)
name[1] = 'Dhinesh'
print(name)

# Tuple ( use () - paranthesis)
name1 = ('Krishna', 'Elan', 'Gokul')
print(name1)
# name1[1] = 'Dhinesh' # It will get a traceback. Because, tuples are unchangable
# print(ame1n)

# Tuples don't have sort,append,reverse function

(name, age) = ('Krishna', 17)
print(name, age)

(a, b) = (12, 34)
print(b)

# Accessing tuples from Dictionaries

names = dict()
names['Krishna'] = 18
names['Elan'] = 19

for x,y in names.items():
    print(x,y)

tups = names.items()
print(tups)

# Comparison of tuples

if (1, 4, 6) < (3, 0, 0):
    print('True')
else:
    print("False")
if ('Krishna', 'Elan') < ('Krishna', 'Elanthiraivel'):
    print('True')
else:
    print('False')

# Sorted lists of tuples

group = {'a':1, 'c':3, 'b':2, 'e':5, 'd':4}
group.items()
print(sorted(group.items()))

# Sorting by Keys

for x,y in sorted(group.items()):
    print(x,y)

# Sorting by values

box = {'a':16, 'b':3, 'c':45, 'd':0}
lst = list()

for key,val in box.items():
    lst.append((val,key))
    lst = sorted(lst, reverse=False)
print(lst)

lst = sorted(lst, reverse=True)

print(lst)

days = ('M','T','W')
print(days[2])

pause()