import mysql.connector
#this module help to connect database
class Databaseconnection():
    def __init__(self):
        self.cur=None
    def connect(self, host, username, password, database, port):
        self.hostname = host
        self.username = username
        self.password = password
        self.database = database
        self.portnum = port

        self.connect = mysql.connector.Connect(host=self.hostname, username=self.username,password=self.password, database=self.database, port=self.portnum)
        self.cur = self.connect.cursor()



