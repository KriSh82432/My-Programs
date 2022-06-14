def pause():
    pauseProgram = input('Press any key to close...')
    
# Accessing strings from lists

# Using loop

print('Using for loop...')
stuff = ['With', 'three', 'words']
for x in stuff:
    print(x)

# Using Split function to convert strings to separate strings in a lists

print('Using split function...')
stuff = 'With three words'
list = stuff.split()
print(list)

# Split features
# It don't care about extra spaces

pack = 'A lot of        spaces      there'
xyz = pack.split()
print(xyz)

# It splits by spaces by default

pack1 = 'Krishna;Elan;Gokul'
xyz = pack1.split()
print(len(xyz),xyz)

# We can command the split to split according to our argument

xyz = pack1.split(';')
print(len(xyz),xyz)

# Finding the day of email received using split function

fhand = open('text.txt')
for line in fhand:
    if not line.startswith('From:'):
        continue
    else:
        x = line.split()
        print(x[2])
# Double splitting pattern
# Finding the host name from email address
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        print(pieces[1])

pause()