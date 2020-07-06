"""
Write a programme read the mailbox data (mbox.txt)
and count the number of email messages per organization
(i.e. domain name of the email address)
using a database with the following schema to maintain the counts.

"""

import sqlite3

conn = sqlite3.connect('new_emaildb1.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

class SqlDatabaseCreation:

    def get_input(self):
        fname = 'mbox.txt'
        if (len(fname) < 1): fname = 'mbox.txt'
        fh = open(fname)
        organisation=[]
        for line in fh:
            if not line.startswith('From: '): continue
            pieces = line.split()
            email = pieces[1]
            new_pieces=email.find('@')
            org=email[new_pieces+1:]
            organisation.append(org)
        return organisation

    def execute_sql(self,organisation):
        for org in organisation:
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                                (org,))
            conn.commit()
        return conn

    def print_result(self):
#https://www.sqlite.org/lang_select.html
        sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
        for row in cur.execute(sqlstr):
            print(str(row[0]), row[1])
        cur.close()

    def processes(self):
        input=self.get_input();
        sql_database=self.execute_sql(input);
        self.print_result()

sql_dataset_1=SqlDatabaseCreation()
sql_dataset_1.processes()
