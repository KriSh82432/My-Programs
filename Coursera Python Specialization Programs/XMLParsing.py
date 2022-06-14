import xml.etree.ElementTree as ET

data = '''<person>
  <name>Krishna</name>
  <age>17</age>
  <date>2004:04:14</date>
  <phone type = "intl">+91 7904148922</phone>
  <email hide = "yes"/>
</person>'''

print('\*.....Program 1.....*/')
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Age:',tree.find('age').text)
print('DOB:',tree.find('date').text)
print('Phone:',tree.find('phone').text)
print('Attribute:',tree.find('email').get('hide'))

# Program to parse XML data which has multiple child tags

stuff = '''<data>
   <users>
     <user x="1">
       <ID>RA2111043010028</ID>
       <name>Krishna V</name>
     </user>
     <user x="2">
       <ID>RA2111043010014</ID>
       <name>Gokul Sidharth</name>
     </user>
     <user x="3">
       <ID>RA2111043010017</ID>
       <name>Sarveshwaran</name>
     </user>
   </users>
</data>
'''

print('\*.....Program 2.....*/')
tree1 = ET.fromstring(stuff)
lst = tree1.findall('users/user')
print('No. of Users:',len(lst))
for word in lst:
    print('Name:',word.find('name').text)
    print('ID  :',word.find('ID').text)
    print('Attr:',word.get('x'))