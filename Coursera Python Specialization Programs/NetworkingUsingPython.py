# Retrieving web pages using socket library
import socket
from types import coroutine

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()

# Using urllib library
# The urllib library does the socket work automatically 

import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file:
    print(line.decode().strip())

# Storing web data in a dictionary
import urllib.request, urllib.parse, urllib.error

files = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for lines in files:
    words = lines.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Web Scrapping using Beautiful soup library

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url  = input('Enter the url:  ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))