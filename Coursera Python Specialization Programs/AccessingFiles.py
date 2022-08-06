def pause():
    pauseProgram = input('Press any key to close...')

file = open('text.txt')
line = file.read()
print(len(line))
print(line[0:21])

for letter in file:
     letter = letter.rstrip()
     if not letter.startswith('From:'):
        continue
     print(letter)

def msg(senders):
   msg = input('Do you want to see the senders name? (y/n)')
   if msg == 'y':
    print(senders)
    print(count,"persons have sent you messages")
   elif msg == 'n':
    print(count,"persons have sent you messages")

file = input('Enter the file name: ')
count = 0 

try:
    fhand = open(file)
except:
    print('File cannot be opened', file)
    quit()

for letter in fhand:
   if letter.startswith('From:'):
       count = count + 1
       #senders = letter
       senders = letter.split()
       senders = senders[1]

msg(senders)


pause()