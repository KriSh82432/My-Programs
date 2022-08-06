# Lists is a data structure

def pause():
    pauseProgram = input('Press any key to close...')

name = ['Krishna', 'Dhinesh', 'Elan']
age = [17, 18, 17]

print(name)
print(age)

print([1, 2,3])
print(['K', 'S', 'E'])
print([]) # A list can be empty

for n in name:
    print("Happy Birthday", n)
print('Done!')

print("Hi", name[1])

name[1] = 'Gokul Sidharth'
print("Hi", name[1])

print(len(name))
print(len(age))

for i in range(len(name)):
    n = name[i]
    print("Happy New Year", n)
    
pause()

names = [ 2, 's']
print(names)