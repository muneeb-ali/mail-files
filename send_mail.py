#!/usr/bin/python
#Last edited by Muneeb Ali on Apr 22, 2010

#---------------------------------------

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import getpass

#---------------------------------------

from config import MAIL_SERVER, MAIL_USER, SEND_DOMAIN, FILE_TYPE
from config import USER_DATABASE, FILES_FOLDER, EMAIL_TEMPLATE 

MAIL_PWD = '' 
MAIL_LOGIN = MAIL_USER.split('@')[0]
EMAIL_SUBJECT = ''
EMAIL_BODY = '' 

#---------------------------------------
def mail(to, subject, text, attach):

   msg = MIMEMultipart()

   msg['From'] = MAIL_USER
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   if (attach != "null.jpg"):
      try:

         part = MIMEBase('application', 'octet-stream')
         part.set_payload(open(attach, 'rb').read())
         Encoders.encode_base64(part)
         part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
         msg.attach(part)
      except:
         print 'Attachment failed'

   mailServer = smtplib.SMTP(MAIL_SERVER, 25)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(MAIL_LOGIN, MAIL_PWD)
   mailServer.sendmail(MAIL_USER, to, msg.as_string())
   
   mailServer.close()

#---------------------------------------
if __name__ == "__main__":

   MAIL_PWD = getpass.getpass('Enter password for ' + MAIL_USER + ': ')

   #------------------------------
   #read the email template 

   fread = open(EMAIL_TEMPLATE,'r')
   email_raw = fread.read()

   email_raw = email_raw.split('<tag>')

   email_subject = email_raw[0]
   email_subject = email_subject.rstrip(' ')
   email_subject = email_subject.rstrip('\n')
   email_subject = email_subject.lstrip(' ')
   email_subject = email_subject.lstrip('\n')
   
   email_body = email_raw[1]
   email_body = email_body.rstrip('\n')
   email_body = email_body.lstrip(' ')
   email_body = email_body.lstrip('\n')
   #------------------------------

   f = open(USER_DATABASE, "r")

   lines = f.readlines()

   for l in lines:
      l  = l.rstrip()
      row = l.split(",")
      name = row[1].lstrip()
      id = row[0]
      email = id + SEND_DOMAIN
      pdf = "./"+ FILES_FOLDER + '/' + id + FILE_TYPE

      #print row
      msg = "Hi " + name + ',\n\n' + email_body

      print "To: " + email
      print 'Subject: ' + email_subject
      print msg
      print '-' * 5

      import time
      time.sleep(1)
      
      if (email != ''):
         #pass
         mail(email, email_subject, msg, pdf)

#***** End of file ***********************************
