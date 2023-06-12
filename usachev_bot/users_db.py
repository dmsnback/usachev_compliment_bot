import sqlite3

con = sqlite3.connect('database')

cur = con.cursor()

cur.execute('''
ALTER TABLE users
DROP COLUMN name
;
''')


con.commit()
con.close()
