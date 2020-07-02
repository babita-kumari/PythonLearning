import sqlite3


con=sqlite3.connect('user_registration.sqlite')
cur=con.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS user_registration(
Name TEXT, 
mobile_no INTEGER, 
email_id TEXT
)
''')
print('table created successfully')
name=input("enter name:")
mobile_no=input("enter mobile.no:")
email_id=input("email_id:")

cur.execute('''INSERT OR IGNORE INTO user_registration(Name, mobile_no, email_id)
        VALUES ( ?, ?,? )''', ( name, mobile_no, email_id, ))

con.commit()
con.close()


