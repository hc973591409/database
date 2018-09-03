import time
from hashlib import sha1

import pymysql

from MysqlClass import MySQLHelper

def main():
    time_start = time.time()
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    acount = input("请输入账户名：")
    paras = [acount]    
    sql = "select * from csdn where account = %s"
    res = insert_data.get_one(sql,paras)
    print(res)
    if res == None:
        print("账号不存在，请核实")
    else:
        pwd = input("请输入密码：")
        if pwd == res[2]:
            print("登陆成功")
        else:
            print("密码错误，请核实")
       

    time_end = time.time()
    print("结束查找，总共花费时间为%0.2f" %(time_end-time_start))



if __name__ == '__main__':
    main()
