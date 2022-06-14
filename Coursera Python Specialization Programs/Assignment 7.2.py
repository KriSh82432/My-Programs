# Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#  compute the average of those values and produce an output as shown below.
#  Do not use the sum() function or a variable named sum in your solution.
# input: mbox-short.txt

def pause():
    pauseProgram = input('Press any key to close...')

file = input("Enter a file name:")
fhandle = open(file)

count = 0
s = 0

for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count += 1
        a = line.find(':')
        x = line[a+1:]
        s = s + float(x)

print("Average:", s/count)
pause()