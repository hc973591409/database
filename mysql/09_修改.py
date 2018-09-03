# 导入包
import pymysql
# 尝试连接数据库
try:
    # 新建处理表格对象
    conn = pymysql.connect(host='192.168.126.129',
                           user='root',
                           password='12345',
                           port=3306,
                           database='stu_info',
                           charset='utf8')
    # 开始
    conn.begin()
    cursor1 = conn.cursor()
    sql = "update student set name='刘邦' where id = 11"
    # 新建sql语句
    count = cursor1.execute(sql)
    # 执行语句
    print(count)
    conn.commit()
    cursor1.close()
    conn.close()
    # 提交
except Exception as identifier:
    raise
