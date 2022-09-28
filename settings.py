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
    'from':'from@mail.com',
    'smtpServer':'smtp.outlook.com',
    'to':'to1@gmail.com,to2@gmail.com',
    'pass': 'pass',
    'subject':'Assunto...',
    'msg':'Mensagem...'
}