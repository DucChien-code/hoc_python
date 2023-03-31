import sqlite3

conn = sqlite3.connect("movies.db")

cur = conn.cursor()
# Uppdate dữ liệu
# sql_command = """ 
# UPDATE movie
# SET year=2000
# WHERE title="Mr. Boot";
# """

sql_command = """
DELETE FROM movie; 
"""
cur.execute(sql_command)

conn.commit()

conn.close()
