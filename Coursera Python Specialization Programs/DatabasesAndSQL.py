import sqlite3

conn = sqlite3.connect('email.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(Email TEXT, Count INTEGER)')

fname = input('Enter file name: ')
if len(fname)<1 : fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if not line.startswith('From'): continue
    piece = line.split()[1]
    cur.execute('SELECT Count FROM Counts WHERE Email=?',(piece,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(Email, Count) VALUES(?,1)',(piece,))
    else:
        cur.execute('UPDATE Counts SET Count = Count + 1 WHERE Email=?',(piece,))
    conn.commit()

sqlc = 'SELECT * FROM Counts ORDER BY Count DESC'

for thing in cur.execute(sqlc):
    print(str(thing[0]),thing[1])

cur.close()