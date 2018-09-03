# 导入包
import pymysql

# 尝试建立链接
try:
    conn = pymysql.connect(host='192.168.126.129',
                           port=3306,
                           database='stu_info',
                           user='root',
                           password='12345',
                           charset='utf8')
    cursor1 = conn.cursor()
    # 新建对象用于操作表格
    conn.begin()
    sql = "insert into student(name) values('张良')"
    # 新建mysql语句
    count = cursor1.execute(sql)
    print(count)
    # 执行
    conn.commit()
    print('连接数据库成功')
except Exception as identifier:
    print(identifier)
