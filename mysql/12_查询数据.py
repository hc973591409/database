# 用一个列表保存参数，只需要把参数传给sql，就知道怎么执行
import pymysql

try:
    conn = pymysql.connect(host='192.168.126.129',
                           port=3306,
                           user='root',
                           password='12345',
                           database='stu_info',
                           charset='utf8')
    conn.begin()
    cursor1 = conn.cursor()
    count=cursor1.execute("select * from student")
    # res = cursor1.fetchone() 获取一条
    # res = cursor1.fetchmany(3) 获取多条，参数为想获取的条数
    res = cursor1.fetchall()
    print(res)
    conn.commit()
    cursor1.close()
    conn.close()
except:
    raise
# cursor对象的execute()方法，也可以用于执行create table等语句
# 建议在开发之初，就创建好数据库表结构，不要在这里执行
