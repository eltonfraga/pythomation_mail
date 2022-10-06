MYSQL = {
    'user':'python',
    'password':'python@123A',
    'host':'localhost',
    'database':'pythest',
    'use_pure':'False'
}

from datetime import datetime
FILE_NAME_XLSX = 'LOGs ' + datetime.today().strftime('%d.%m.%y')+'.xlsx'
SHEET_NAME_XLSX = 'sheet'

MAIL = {
    'from':'from@outlook.com',
    'smtpServer':'smtp-mail.outlook.com',
    'to':'to@gmail.com',
    'pass': 'yourPassHere',
    'port': 587,
    'subject':'Subject...',
    'msg':'Message...'
}
