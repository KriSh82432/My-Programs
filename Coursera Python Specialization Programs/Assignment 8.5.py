# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and
#  if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

def pause():
    pauseProgram = input('Press any key to close...')

file = input('Enter a file name: ')
fhand = open(file)
lst = list()
sp = list()

for line in fhand:
    sp = line.split()
    for z in sp:
       if not z in lst:
         lst.append(z)

lst.sort()
print(lst)

pause()