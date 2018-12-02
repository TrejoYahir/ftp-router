import telnetlib
from ftplib import FTP


def get_config_file(path, ip):
    try:
        tn = telnetlib.Telnet(ip)
        user = "rcp"
        password = "rcp"
        tn.read_until("User: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("copy run start\n")
        tn.write("exit\n")
        tn.write("exit\n")
        print tn.read_all()
        tn.close()
        ftp = FTP()
        ftp.connect(ip, 21)
        ftp.login('rcp', 'rcp')
        print ftp.getwelcome()
        fl = open(path+"/startup-config.txt", 'wb')
        ftp.retrbinary('RETR %s' % 'startup-config', fl.write)
        fl.close()
        ftp.quit()

    except Exception as e:
        print e
