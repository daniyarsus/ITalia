import sqlite3 as sq

with sq.connect("shop.db") as con:

    cursor = con.cursor()

    cursor.execute("""CREATE TABLE users (
        name TEXT,
        sex TEXT,
        old INTEGER,
        score INTEGER
    )""")



#connect.close() не желательно