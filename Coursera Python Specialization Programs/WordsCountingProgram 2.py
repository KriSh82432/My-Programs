# Words counting program
# For finding in a .txt file

def pause():
    pauseProgram = input('Press any key to close...')

fname = input('Enter a file name: ')
hand = open(fname)
counts = dict()

for line in hand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or bigCount < count:
        bigCount = count
        bigWord = word

print("Most used word is", bigWord,", which is used by", bigCount,"times")

pause()