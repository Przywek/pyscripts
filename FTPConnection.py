from ftplib import FTP
import os
ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents
ftp.retrbinary('RETR README', open('README', 'wb').write) # copy file from server
file = open('kitten.jpg','rb')
ftp.storbinary('STOR kitten.jpg', file)  # send file to server
ftp.quit()
def uploadFileFTP(sourceFilePath, destinationDirectory, server, username, password):
    myFTP = FTP(server, username, password)
    if destinationDirectory in [name for name, data in list(myFTP.mlsd())]:
        print ("Destination Directory does not exist. Creating it first")
        myFTP.mkd(destinationDirectory)
    # Changing Working Directory
    myFTP.cwd(destinationDirectory)
    if os.path.isfile(sourceFilePath):
        fh = open(sourceFilePath, 'rb')
        myFTP.storbinary('STOR %s' % fh)
        fh.close()
    else:
        print ("Source File does not exist")
