"""
    将数据库封装一个类，将server 需要的数据库操作功能分别写成方法，在server中实例化对象
"""
import pymysql, hashlib

SALT = '$%@#DF'
class Database:
    def __init__(
            self,
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8mb4',
            database='electronic_dic'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            database=self.database,
            charset=self.charset)
        self.cur = self.db.cursor()
        self.connect_database()

    def connect_database(self):
        pass

    def close(self):
        self.db.close()

    def create_cursor(self):
        pass

    def register(self, name, passwd):
        sql = "select * from user where name = '%s' "%name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False
        hash = hashlib.md5((name+SALT).encode())
        hash.update(passwd.encode())
        # user a different variable name to make sure the password encrypted can be added into database correctly
        passwd_encryption = hash.hexdigest()
        sql = "insert into user (name, passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd_encryption])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, passwd):
        # hash = hashlib.md5((name + SALT).encode())
        # hash.update(passwd.encode())
        # passwd = hash.hexdigest()
        sql = "select * from user where name = '%s' and passwd = '%s'"%(name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

# a = Database()
# print(a.login('test01','123123'))