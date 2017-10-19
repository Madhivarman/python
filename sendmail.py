import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr  = "madhivarman451@gmail.com"
toaddr = "madhivarman451@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "This email is automatically generated..!"

body = "Hello...! This email is automatically generated so never mind"

msg.attach(MIMEText(body,'plain'))

filename = "sendmail.py"
attachment = open("/root/Desktop/python/sendmail.py","rb")

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('content-Disposition',"attachment;filename=%s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"*******")   # * represents your gmail password
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
