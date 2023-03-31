import logging
logging.basicConfig(filename='..//Logger//capstone.log',level=logging.DEBUG,format=('%(asctime)s-%(name)s-%(levelname)s-%(message)s'))
from searchFileinDrives.searchfiles import SearchFilesDrives
from searchindb.DBconnection import Databaseconnection
from searchindb.searchFilepath import SearchFile
from capstoneExceptions.MysqlException import MySqlError
from searchindb.InsertData import InsertFilesDB
import mysql.connector
import time
import openpyxl as xl
def userdata():
    dir=input("Enter the drive like c:// d:// \n")
    filename=input("Enter the filename with extension like demo.txt \n")
    logging.info(f"Drive name{dir} file name{filename}")
    dbobj=SearchFile()
    logging.info(f"class used{SearchFile.__name__}")
    wb = xl.load_workbook("c://testdata//Testfiles.xlsx")
    ws=wb.active
    try:
        dbobj.connect("localhost","root","Vanitha@143","myhcl",3306)
        logging.info("myhcl database is connected")
        result=dbobj.search(filename)
    except mysql.connector.Error as err:
        logging.exception(err, exc_info=True)
        raise MySqlError(f'{err.msg}',err.errno)

    finally:
        dbobj.connect.close()
    if len(result)==0:
        print("Not found in database")
        print("Now searching in Drives...")
        logging.info("Not Found in Database")
        logging.info("Now searching in Drives")
        start_time=time.time()
        obj=SearchFilesDrives()
        logging.info(f'for searching in drive {SearchFilesDrives.__name__} is used')
        files=obj.searchfiles(dir,filename)

        ws.cell(row=1,column=1).value=str(files)
        wb.save("c://testdata//Testfiles.xlsx")
        wb.close()
        inserobj=InsertFilesDB()
        inserobj.insert(files)
        logging.info(f'files found {files}')
        print(files)
        #print(obj.searchfiles(dir,filename))
        obj.start()
        end_time=time.time()
        logging.info(f'time taken{end_time-start_time}')
        logging.info("Ending")
        print(end_time-start_time)
    else:
        print("Found in database")
        print(result)
userdata()