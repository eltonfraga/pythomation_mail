import argparse,json
import os
import pandas as pd
import mysql.connector
import settings as se
from MyMailer import MyMailer

parser = argparse.ArgumentParser()

parser.add_argument("-q", "--query", help="define wich query will run")
parser.add_argument("-db", "--database", help="define wich database server use")
parser.add_argument("-mg", "--mailgroup", help="define list of mail to send")

args = parser.parse_args()

queryArg = args.query if args.query else 'default'
queryFile = open(f'./queries/{queryArg}.sql','r')
query = queryFile.read()
queryFile.close()

dbArg = args.database if args.database else 'default'
dbJson = open(f'./dbs/{dbArg}.json')
db=json.load(dbJson)
dbJson.close()

mailgroupArg = args.mailgroup if args.mailgroup else 'default'
mailGroupFile = open(f'./mail_list/{mailgroupArg}.txt','r')
mailGroup = mailGroupFile.read().replace('\n', ' ')
mailGroupFile.close()


#### BEGIN CONNECTING WITH DATABASE AND FETCHING DATA FROM QUERY
try:
    conn = mysql.connector.connect(**db)
    cursor = conn.cursor()
    cursor.execute(query)
    queryResult = cursor.fetchall()
except:
    print('Check your database instance and/or your config file.')    
#### END CONNECTING WITH DATABASE AND FETCHING DATA FROM QUERY

#### BEGIN EXPORTING .xlsx FILE
#os.remove(se.FILE_NAME_XLSX)
try:
    columnNamesXLSX = [desc[0] for desc in cursor.description]
    outputXLSX = pd.DataFrame(list(queryResult),columns=columnNamesXLSX)
    writerXLSX = pd.ExcelWriter(se.FILE_NAME_XLSX)
    outputXLSX.to_excel(writerXLSX,sheet_name=se.SHEET_NAME_XLSX)
    writerXLSX.close()
except:
    print('File couldn\'t be opened or writed.' )    
#### BEGIN EXPORTING .xlsx FILE

cursor.close()
conn.close()

#### BEGIN MAILER
try:
    myMailer = MyMailer(se.MAIL)
    myMailer.attachFile(se.FILE_NAME_XLSX)
    myMailer.sendMail(se.MAIL['smtpServer'],se.MAIL['port'],se.MAIL['pass'],mailGroup)
except:
    print('Error when try to send mail.')    
#### END MAILER

#### CLEANING FILE
os.remove(se.FILE_NAME_XLSX)