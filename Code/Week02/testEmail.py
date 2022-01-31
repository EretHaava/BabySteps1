# Send an email via Gmail
# Author Eret Haava

print ('in testEmail')
import smtplib

username = 'eret.haava@gmail.com'
password = 'EretHaava261280'
toEmail = 'eret.haava@gmail.com'
message = 'Hi There!'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(username,toEmail,message)
