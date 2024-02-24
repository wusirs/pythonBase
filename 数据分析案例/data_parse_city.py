import json
from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='WL',
    password='1234zxcv'
    # , autocommit=True
)

cursor = conn.cursor()

conn.select_db('common')

json_file_reader: str = open('postCode.json', 'r', encoding='utf8').readline()
city_json: list = json.loads(json_file_reader)

for item in city_json:
    insert_sql = (
        ("insert into city_code(id, province, city, area, post_code, area_code)"
         "      values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')")
        .format(item['id'], item['province'], item['city'],
                item['area'], item['post_code'], item['area_code']))
    cursor.execute(insert_sql)

# 手动提交
conn.commit()
conn.close()
