import time
import os
# Function to pause the terminal
def pause():
    programPause = input("Press any key to continue")

print('Hello World')
num=float(input('Enter the number: '))
num_sqrt=num**0.5
print('The square root of %0.3f is %0.3f'%(num,num_sqrt))
a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# Conditional Statement
if (area>=0):
    print("Area is positive")
else :
    print("Area is negative")

# While loop
while (area>0):
    print('Area is greater than zero')
    area=area-1
# Command to pause the terminal for a certain period of time
print(area,s)
time.sleep(10)
pause()
exit()