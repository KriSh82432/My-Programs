# Program to print the 10 most used words in a file

def pause():
    pauseProgram = input('Press any key to close...')

fhand = open('Poem.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

for key,val in counts.items():
    tups = (val,key)
    lst.append(tups)

lst = sorted(lst, reverse=True)
print("Top 10 most used words are: ")
count = 0

for val,key in lst[:10]:
    count += 1
    print(count,key,val)

pause()