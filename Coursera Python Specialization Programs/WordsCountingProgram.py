# Words counting program
# For finding in a single line

def pause():
    pauseProgram = input('Press any key to close...')


print("Enter a line:")
line = input('')
counts = dict()

words = line.split()

print("Splitted Line:", words)
print("Counting is in progress...")

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

pause()
