# 用一个列表保存参数，只需要把参数传给sql，就知道怎么执行
import pymysql

try:
    conn = pymysql.connect(host='192.168.126.129',
                           port=3306,
                           user='root',
                           password='12345',
                           database='stu_info',
                           charset='utf8')
    name = input("请输入要插入的名字")
    conn.begin()
    cursor1 = conn.cursor()
    parameter=[name]
    count=cursor1.execute("insert into student(name) values(%s)",parameter)
    print(count)
    conn.commit()
    cursor1.close()
    conn.close()
except:
    raise
# cursor对象的execute()方法，也可以用于执行create table等语句
# 建议在开发之初，就创建好数据库表结构，不要在这里执行
