dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'diudiu',
            'database': 'vsearchlogDB'}

import mysql.connector

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
