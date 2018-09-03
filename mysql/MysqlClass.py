import pymysql


class MySQLHelper(object):
    def __init__(self, host, port, database, user, password, charset='utf8'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port,
                                    database=self.database, user=self.user, password=self.password, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def is_ok(self):
        self.conn.commit()

    def get_one(self, sql, params=[]):
        res = None
        self.connect()
        try:
            self.cursor.execute(sql, params)
            res = self.cursor.fetchone()
            if res:
                return res
        except:
            raise
        return res

    def get_all(self, sql, params=[]):
        self.connect()
        res = ()
        try:
            self.cursor.execute(sql, params)
            res = self.cursor.fetchall()
            if res:
                return res
        except:
            raise
        finally:
            self.close()
        return res

    def edit(self, sql, params):
        try:
            self.cursor.execute(sql, params)
        except:
            raise


def main():
    Mysql_op = MySQLHelper('192.168.126.129', 3306,
                           'stu_info', 'root', '12345')
    sql = "insert into student(name,gender) values(%s,%s)"
    name = input("请输入名字:")
    gender = input("请输入性别，1为男，0为女")
    parameters = [name, bool(gender)]
    count = Mysql_op.edit(sql, parameters)
    if count:
        print("插入成功")
    else:
        print("插入失败")

def main1():
    Mysql_op = MySQLHelper('192.168.126.129', 3306,
                           'stu_info', 'root', '12345')
    sql = "select * from student"
 
    count = Mysql_op.get_all(sql)
    if count:
        print(count)
    else:
        print("查询失败")


if __name__ == '__main__':
    main()
