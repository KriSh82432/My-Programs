from os import error

def error():
    print("No")
def pause():
    programPause = input('Press any key to close...')

name = input("Enter your name: ")
print(name[:])

for letter in name:
    print(letter)

index = 0

while index < len(name):
    letter = name[index]
    print(index, letter)
    index += 1

if 'Krish  na' in name:
   print("Found it!!")
else:
    print("Not Found")

if name == 'Krishna':
    print("Alright, no problem")
elif name < 'Krishna':
    print("Hey, " + name + ",comes before Krishna")
elif name > 'Krishna':
    print("Hey, " + name + ",comes after Krishna")
else:
    print("Alright, no problem")

print(name.replace('k','i'))
print(name.lower())
print(name.upper())
print(name.find('h'))
print(name.rstrip())
print(name.lstrip())
print(name.strip())

if name.startswith('K'):
    print("Yes,it starts with K")
else :
    error()

pause()