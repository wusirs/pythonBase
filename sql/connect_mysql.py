from pymysql import Connection

# 获取到mysql数据库的连接对象

conn = Connection(host='localhost', port=3306, user='root', password='j13655671361')

# 打印mysql数据库软件信息
print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()

# use py_db_1;
conn.select_db('py_db_1')

# cursor.execute('create table test_1(id int)')

cursor.execute('select * from student')

res: tuple = cursor.fetchall()
print(res)


# 查询



conn.close()
