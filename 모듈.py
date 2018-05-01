from ftplib import FTP
ftp=FTP("ftp1.at.proftpd.org")
ftp.login()

ftp.retrlines('LIST')