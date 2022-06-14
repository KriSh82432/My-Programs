# Regular Expressions 
import re

# search function

hand = open('mbox-short.txt')
for line in hand:
    line.rstrip()
    if re.search('^F.*' , line):
        print(line)
    if re.search('^X.*', line):
        print(line)
    if re.search('^X-\S+:', line):
        print(line)

# findall function

x = 'My favourite numbers are 18 and 7'
y = re.findall('[0-9]', x) # it will print numbers in  single digit
print(y)

# The expected output will be ['1', '8', '7']

z = re.findall('[0-9]+', x) # The + character will look for multiple digits 
print(z)

# The exoected output will be ['18', '7']

a = 'From: Using the : express'
b = re.findall('^F.+:', a) # This will print the full string because, if a same character comes twice in a 
# string, the + character gives the maximum repeating character
print(b)

c = re.findall('^F.+?:', a) # The ? character will give the least repeating character
print(c)

mail = 'From loneworker@gmail.com Jan Sat 10:59 sent'
d = re.findall('\S+@\S+', mail) # This will give the whole email address because, it's a greedy character
print(d)

e = re.findall('\S+@\S+?', mail) # This will give 'loneworker@g' because, ? is a non-greedy character
print(e)

# Using ()

f = re.findall('^From (\S+?@\S+)', mail) # The characters inside the paranthesis will only print
print(f)

# Printing the host name of email address using split function
splitt = mail.split()
frag = splitt[1]
piece = frag.split('@')
print(piece[1])

# Using regular expressions
g = re.findall('@([^ ]*)', mail)
print(g)
 # Tuned version
h = re.findall('^From .*@([^ ]*)', mail)
print(h)

# Program to search through multiple lines and extract the data
numlist = list()
handle = open('mbox-short.txt')

for lin in handle:
    lin = lin.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lin)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))

i ='I have $10.20 dollars'
k = re.findall('^I\shave\s(\$[0-9.]+)', i)
print(k)