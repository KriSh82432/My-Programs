# Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.
# Input file name: mbox-short.txt

from typing import Counter


def pause():
    pauseProgram = input('Press any key to close...')

name = input('Enter a file name: ')
handle = open(name)
mails = dict()
lst = list()

for line in handle:
    if line.startswith('From '):
        mail = line.split()
        lst.append(mail[1])

for word in lst:
    mails [word] = mails.get(word, 0) + 1

maxSender = None
maxCount = None

for key,val in mails.items():
    if maxCount is None or maxCount < val:
        maxSender = key
        maxCount = val

print(maxSender, maxCount)
pause()