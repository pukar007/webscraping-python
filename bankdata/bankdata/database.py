import sqlite3

conn= sqlite3.connection ('data.db')


curs = conn.cursor()


curs.execute("""create  table data_db(


title text,
sno number,
particulars text,
details text,
charges text
)""")


conn.commit()
conn.close()








