# Manipulating lists

def pause():
    pauseProgram = input("Press any key to close...")

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

#Concatenating
print(a+b)

#Slicing
print(a[1:4])
print(b[:5])
print(a[:])

#append things 
c = list()
c.append('Gokul')
c.append('Dhinesh')
c.append('Krishna')
print(c)

#in operator
if 1 in a:
    print('True')
if 3 not in b:
    print('False')

#sorting 
c.sort()
print(c)
pause()