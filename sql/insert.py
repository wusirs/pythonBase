from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='1qa2ws'
    # , autocommit=True
)

cursor = conn.cursor()

conn.select_db('pydata')

cursor.execute("insert into student values(3,'王二', 14)")

# 手动提交
conn.commit()

conn.close()
