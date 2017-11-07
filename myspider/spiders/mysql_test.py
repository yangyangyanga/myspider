import pymysql

conn = pymysql.Connect(host='127.0.0.1', port=3306,db='test',
                       user='root', password='yangyaxia',charset='utf8' )

cursor = conn.cursor()
cursor.execute('select * from student')

data = cursor.fetchall()
# print(data)

cursor.close()
conn.close()