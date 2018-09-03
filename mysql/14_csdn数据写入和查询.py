import pymysql
from MysqlClass import MySQLHelper
import re


def main1():
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    sql = "create table csdn(id int auto_increment primary key not null, account varchar(20), passwd varchar(20), email varchar(40))"
    insert_data.edit(sql, [])


def main():
    insert_data = MySQLHelper('192.168.126.129', 3306,
                              'stu_info', 'root', '12345')
    sql = "insert into csdn(account,passwd,email) values(%s,%s,%s)"
    f = open('csdn.txt', 'r', encoding='utf-8')
    if not f:
        print("打开失败")

    while True:
        try:
            string = f.readline()
            pattern = re.compile(" # ")
            paras = re.split(pattern, string)
            if len(string) <= 0:
                print("读取完成")
                break
            else:
                # print(paras)
                insert_data.edit(sql, paras)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()


# str1 = 'zdg # 12344321 # zdg@csdn.net'
# count = str1.count('#')
# print(count)
# str2=(''.join(str1.split())).split('#')

# print(str2)
