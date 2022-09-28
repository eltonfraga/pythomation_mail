import sys
import os
import pandas as pd
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import settings as se
import queries
#import csv

#external = sys.argv[1]
#query = queries.QUERY["query_2"] + external

#### BEGIN CONNECTING WITH DATABASE AND FETCHING DATA FROM QUERY
conn = mysql.connector.connect(**se.MYSQL)
query = queries.QUERY["query_1"]
cursor = conn.cursor()
cursor.execute(query)
queryResult = cursor.fetchall()
#### END CONNECTING WITH DATABASE AND FETCHING DATA FROM QUERY

#### BEGIN EXPORTING .csv FILE
#columnNamesCSV = [(desc[0] for desc in cursor.description)]
#outputCSV = open('./file_to_send.csv','w')
#fileHandler = csv.writer(outputCSV,delimiter=';')
#fileHandler.writerows(columnNamesCSV)
#fileHandler.writerows(queryResult)
#outputCSV.close()
#### END EXPORTING .csv FILE

#### BEGIN EXPORTING .xlsx FILE
columnNamesXLSX = [desc[0] for desc in cursor.description]
outputXLSX = pd.DataFrame(list(queryResult),columns=columnNamesXLSX)
writerXLSX = pd.ExcelWriter(se.FILE_NAME_XLSX)
outputXLSX.to_excel(writerXLSX,sheet_name=se.SHEET_NAME_XLSX)
writerXLSX.save()
writerXLSX.close()
#### BEGIN EXPORTING .xlsx FILE

cursor.close()
conn.close()

#### BEGIN MAILER
mail = MIMEMultipart()
mail['From'] = se.MAIL['from']
mail['To'] = se.MAIL['to']
mail['Subject'] = se.MAIL['subject']
mail.attach(MIMEText(se.MAIL['msg'], 'plain'))

attachment = open(se.FILE_NAME_XLSX,'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % se.FILE_NAME_XLSX)

mail.attach(part)

attachment.close()
mailer = smtplib.SMTP(se.MAIL['smtpServer'],587)
mailer.starttls()
mailer.login(se.MAIL['from'],se.MAIL['pass'])
mailer.sendmail(se.MAIL['from'],se.MAIL['to'],mail.as_string())
mailer.quit()
#### END MAILER

os.remove(se.FILE_NAME_XLSX)