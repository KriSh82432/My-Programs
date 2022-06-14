import sqlite3

connection = sqlite3.connect('Email-1.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS COUNTS')
cursor.execute('CREATE TABLE COUNTS(org TEXT, count INTEGER)')

fname = input('Enter the file name:')
if len(fname) < 1 : fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From') : continue
    part = line.split()[1]
    parts = part.split('@')[-1]
    cursor.execute('SELECT count FROM COUNTS WHERE org=?',(parts,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO COUNTS(org, count) VALUES(?,1)',(parts,))
    else:
        cursor.execute('UPDATE COUNTS SET count = count + 1 WHERE org=?',(parts,))
    connection.commit()

sqlcomm = 'SELECT org, count FROM COUNTS ORDER BY count DESC'

for row in cursor.execute(sqlcomm):
    print(str(row[0]),row[1])