import sqlite3

conn = sqlite3.connect("books.db")

cur = conn.cursor()

sql_comand = """
INSERT INTO book (name, author) VALUES (?, ?)
"""

lst = [ # list[tuple]
    ("Python in agree", 'Ooo')
]

cur.executemany(sql_comand, lst)
conn.commit()

conn.close()