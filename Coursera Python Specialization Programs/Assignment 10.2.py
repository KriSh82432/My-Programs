# Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
#  then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

def pause():
    pauseProgram = input('Press any key to close...')

name = input('Enter a file name: ')
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From '):
      time = line.split()[5].split(":")
      counts[time[0]] = counts.get(time[0], 0) + 1

lst = list()
for key,val in counts.items():
    lst.append((key,val))

lst.sort()

for hour,count in lst:
    print(hour,count)

pause()
