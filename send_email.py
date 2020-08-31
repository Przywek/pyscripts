import smtplib
# establish a connection to smtp server
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
# start tls connection
conn.starttls()
# use credentials to login
conn.login('xx@xxx.com', 'xx@xxx')
# sendmail \n\n to skip to next line must have subject and \n\n
conn.sendmail('xx@gmail.com','karol.przywarty@gmail.com', 'Subject: So Long..\n\n Dear All, \n ferwell friend.\n\n AL')
# quit connection
conn.quit()
