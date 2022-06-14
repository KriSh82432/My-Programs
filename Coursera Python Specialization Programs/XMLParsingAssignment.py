from gettext import find
import xml.etree.ElementTree as ET
import urllib.request, urllib.error, urllib.parse

def pause():
    pauseProgram = input('Enter any key to close...')

url = input('Enter any url: ')
xml = urllib.request.urlopen(url).read()  
data = ET.fromstring(xml)
countList = data.findall('comments/comment/count')

sum = 0
for count in countList:
      sum  += int(count.text)

print(sum)

pause()