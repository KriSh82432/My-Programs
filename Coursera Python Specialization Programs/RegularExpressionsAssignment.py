import re

file = open('actual.txt')
text = file.read()

num = re.findall('[0-9]+', text)
sum = 0
print(num)
for i in num:
    i = int(i)
    sum += i

print(sum)

file.close()