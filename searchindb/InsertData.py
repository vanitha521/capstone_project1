from searchindb.DBconnection import Databaseconnection
from capstoneExceptions.MysqlException import MySqlError
import mysql.connector
class InsertFilesDB(Databaseconnection):
    def __init__(self):
        self.con = self.connect('localhost','root','Vanitha@143','myhcl',3306)
    def insert(self,files):

        #this method takes files from drives and insert into database
        self.files=files
        self.insertcur=self.connect.cursor()
        for f in self.files:
            sql="insert into fileinfo(filename) values(%s)"
            self.insertcur.execute(sql,(f,))
            self.connect.commit()
        print("Files added Successfully")
# try:
#     f=["hema","sirii"]
#     obj=InsertFilesDB()
#     print(obj)
# except mysql.connector.Error as err:
#     raise MySqlError(f'{err.msg}',err.errno)




