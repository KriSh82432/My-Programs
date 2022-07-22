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
