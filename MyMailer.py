import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#### BEGIN MAILER
class MyMailer:
    def __init__ (self,items):
        self.mail = MIMEMultipart()
        self.mail['From'] = items['from']
        self.mail['Subject'] = items['subject']
        self.mail.attach(MIMEText(items['msg'], 'plain'))

    def attachFile(self,fileName):
        attachment = open(fileName,'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
        self.mail.attach(part)
        attachment.close()

    def sendMail(self,server,port,passwd,destinatary):
        mailer = smtplib.SMTP(server,port)
        mailer.starttls()
        mailer.login(self.mail['From'],passwd)
        mailer.sendmail(self.mail['From'],destinatary,self.mail.as_string())
        mailer.quit()
#### END MAILER