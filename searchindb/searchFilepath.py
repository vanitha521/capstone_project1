import mysql.connector
from searchindb.DBconnection import Databaseconnection
from capstoneExceptions.MysqlException import MySqlError
class SearchFile(Databaseconnection):#this class will help to find file
    def search(self,filename):
        self.filename=filename
        sql="select * from fileinfo where filename like  '%{0}'".format(filename)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
