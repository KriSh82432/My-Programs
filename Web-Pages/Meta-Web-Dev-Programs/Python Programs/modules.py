import sys, calendar

location = sys.path
print(location)
for i in location: 
    print(i)

leapDays = calendar.leapdays(200, 2200)
isLeap = calendar.isleap(2016)
print(leapDays)
print(isLeap)