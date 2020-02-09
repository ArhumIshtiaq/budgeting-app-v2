import sqlite3 as sq3

dbFile = "userData.sqlite"
table1 = "dummyUser"
column1 = "Label"
column2 = "Value"
fieldType1 = 'TEXT'
fieldType2 = 'INTEGER'

conn = sq3.connect(dbFile)
c = conn.cursor()

c.execute('CREATE TABLE {tn}  ({c1} {ft1})'
          .format(tn=table1, c1=column1, ft1=fieldType1))

c.execute("ALTER TABLE {tn} ADD COLUMN '{c2}' {ft2}"
          .format(tn=table1, c2=column2, ft2=fieldType2))

conn.commit()
conn.close()
