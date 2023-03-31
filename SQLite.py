# SQLite: *.db là một CSDL nằm trên ổ cứng được biểu diễn bởi 1 flie.db, dùng để lấy thông tin từ CSDL
import sqlite3

conn = sqlite3.connect("movies.db")

cur = conn.cursor() # con trỏ đến giá trị

sql_command = "SELECT * FROM movie;"

cur.execute(sql_command)

lst = cur.fetchall() # Lấy ra tất cả 1 lần
print(lst)

for line in cur: # lấy 1 bảng ghi tại 1 thời điểm
    print(line)

print(cur.fetchone()) # Lấy ra 1 bản ghi hàng đầu tiền

conn.commit()

conn.close()
