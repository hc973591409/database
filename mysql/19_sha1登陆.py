import time
from hashlib import sha1

import pymysql

from MysqlClass import MySQLHelper

def main():
    time_start = time.time()
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    print("="*50)
    acount = input("请输入账户名：")
    paras = [acount]    
    sql = "select * from csdn_sha1 where account = %s"
    res = insert_data.get_one(sql,paras)
    print(res)
    if res == None:
        print("+"*50)
        print("账号不存在，请核实")
    else:
        print("+"*50)
        pwd = input("请输入密码：")
        # 加密算法
        s = sha1()
        s.update(pwd.encode('utf-8'))
        pwd = s.hexdigest()
        print(pwd)

        # 与数据库中已经加密过的对比
        if pwd == res[2]:
            print("+"*50)
            print("登陆成功")
        else:
            print("+"*50)
            print("密码错误，请核实")
       

    time_end = time.time()
    # print("结束查找，总共花费时间为%0.2f" %(time_end-time_start))



if __name__ == '__main__':
    main()
