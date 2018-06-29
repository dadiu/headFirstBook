dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'diudiu',
            'database': 'vsearchlogDB'}

import mysql.connector

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s,%s,%s,%s,%s)"""
cursor.execute(_SQL, ('account', 'aeiou', '127.0.0.1', 'Chrome', "{a,o,u}"))

conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
