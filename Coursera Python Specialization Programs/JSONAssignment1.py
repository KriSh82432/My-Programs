#In this assignment you will write a Python program
#The program will prompt for a URL, read the JSON data from that URL
#  using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where 
# we give you the sum for your testing and the other is the actual data
#  you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1400405.json (Sum ends with 34)

import urllib.parse, urllib.request, urllib.error
import json

url = input('Enter the url: ')
print('Retrieving',url)
url2 = urllib.request.urlopen(url)
data = url2.read()
print('Retrieved',len(data),'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))

sum = 0
for stuff in js['comments']:
    sum += int(stuff['count'])
print(sum)
