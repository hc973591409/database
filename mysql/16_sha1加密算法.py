import re
import time
from hashlib import sha1

import pymysql

from MysqlClass import MySQLHelper


def main3():
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    sql = "create table csdn_sha1(id int auto_increment primary key not null, account varchar(20), passwd char(40), email varchar(45))"
    insert_data.edit(sql, [])

def main_demo():
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    sql = "insert into student(name) values('刘备')"
    insert_data.edit(sql, [])
    insert_data.is_ok()
    print('插入完成')

def main_test():
    string = 'mochunning # 12345678 # mo.chunning@163.com'
    pattern = re.compile(' # ')
    s_list = re.split(pattern,string)

    # 新建加密对象
    s = sha1()
    s.update(s_list[1].encode('utf-8'))
    s_list[1] = s.hexdigest()
    print(s_list)

def main():
    time_start = time.time()
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    sql = "insert into csdn_sha1(account,passwd,email) values(%s,%s,%s)"
    f = open('csdn.txt', 'r', encoding='utf-8')
    if not f:
        print("打开失败")
    print("插入数据")
    while True:
        
        try:
            string = f.readline()
            pattern = re.compile(" # ")
            paras = re.split(pattern, string)

            # 新建加密对象
            s = sha1()
            s.update(paras[1].encode('utf-8'))
            paras[1] = s.hexdigest()

            if len(string) <= 0:
                print("读取完成")
                break
            elif len(paras):
                insert_data.edit(sql, paras)
                insert_data.is_ok()
        except Exception as e:
            print(e)
            pass

    time_end = time.time()
    print("结束插入，总共花费时间为%0.2fh" %((time_end-time_start)/360))


if __name__ == '__main__':
    main()


# str1 = 'zdg # 12344321 # zdg@csdn.net'
# count = str1.count('#')
# print(count)
# str2=(''.join(str1.split())).split('#')

# print(str2)
