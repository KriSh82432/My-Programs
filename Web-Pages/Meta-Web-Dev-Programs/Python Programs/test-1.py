import time
start_time = time.time()

num_list = [33, 42, 5, 66, 77, 22, 16, 79,
            36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
over = list()
under = list()
count = 0

for index, num in enumerate(num_list):
    if num >= 45:
        over.append(num)
    elif num == 36:
        print(num, " found at position ", index+1)
    else:
        under.append(num)
    count += 1

print("Over 45", over)
print("Under 45", under)
print(f"Count : {count}")

# Lists

num1 = [1, 2, 3, 4, 5]

num1.insert(3, 5)
print(*num1)

num1.append(6)
print(*num1)
num1.append([7,8])
print(*num1)

num1.extend([9,10,11])
print(*num1)
num1.pop(7)
print(*num1)
num1.insert(1, 'Krishna')
num1.append(3)
print(*num1)
print(num1.count(3))
print(num1.index(3))

#Sets

set_a = {1, 2, 3, 4, 5, 5} #Set removes duplicate values
print(set_a)
set_a.add(6)
print(set_a)
set_a.discard(2)
print(set_a)
set_a.remove(3)
print(set_a)

set_b = {1, 2, 3, 4, 5}
set_c = {3, 4, 5, 6, 7}
print(set_b.union(set_c))
print(set_b | set_c)
print(set_b.intersection(set_c))
print(set_b & set_c)
print(set_b.difference(set_c))
print(set_b - set_c)
print(set_c.difference(set_b))
print(set_c - set_b)
print(set_b.symmetric_difference(set_c))
print(set_b ^ set_c)

#Dictionaries

series = {1:'Game of Thrones', 2:'Peaky Blinsders', 3:'Breaking Bad', 4:'Money Heist', 5:'Vikings'}
print(series)
series[5] = 'Stranger Things'
print(series)
del series[5]
print(series)
for key,item in series.items():
    print(key, item)

with open("D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\sampletext.txt", 'r') as file:
    data = file.read()
    print(data)
print(round(time.time()-start_time, 4))