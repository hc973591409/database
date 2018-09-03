# python3.x如何安装MySQL-python（MySQLdb）？
# pip install PyMySQL

# ?在文件中引入模块
# import mysqldb

# Connection对象

# 用于建立与数据库的连接
# 创建对象：调用connect()方法
# conn=connect(参数列表)
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数db：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，默认是'gb2312'，要求与数据库创建时指定的编码一致，否则中文会乱码

# 对象的方法
# close()关闭连接
# commit()事务，所以需要提交才会生效
# rollback()事务，放弃之前的操作
# cursor()返回Cursor对象，用于执行sql语句并获得结果

# cursor对象：
#     执行sql语句
#     创建对象：调用Connection对象的cursor()方法

# cursor1=conn.cursor()

# 对象的方法
# close()关闭
# execute(operation [, parameters ])执行语句，返回受影响的行数
# fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
# next()执行查询语句时，获取当前行的下一行
# fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
# scroll(value[,mode])将行指针移动到某个位置
# mode表示移动的方式
# mode的默认值为relative，表示基于当前行移动到value，value为正则向下移动，value为负则向上移动
# mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0

# 对象的属性
# rowcount只读属性，表示最近一次execute()执行后受影响的行数
# connection获得当前连接对象

import pymysql
conn = pymysql.connect(host='192.168.126.129',
                       user='root',
                       password='12345',
                       database='stu_info',
                       charset='utf8')
cursor = conn.cursor()
sql = 'select * from subjects'
cursor.execute(sql)
rs = cursor.fetchall()
print(rs)

print("导入成功")
