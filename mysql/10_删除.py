# 导包
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
    sql = "delete from student where name='刘邦'"
    count = cursor1.execute(sql)
    print(count)
    conn.commit()
    cursor1.close()
    conn.close()
except Exception as identifier:
    pass
