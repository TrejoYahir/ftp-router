import telnetlib
from ftplib import FTP
import os


def make_connection(ip, path):
    ftp = FTP()
    try:
        ftp.connect(ip, 21)
        ftp.login('rcp', 'rcp')
        print ftp.getwelcome()
        fl = open(path + "/startup-config.txt", 'r')
        ftp.storbinary('STOR ' + "startup-config.txt", fl)
        fl.close()
        ftp.quit()
    except Exception as e:
        print e
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
    tn.write("copy startup-config.txt startup-config\n")
    tn.write("exit\n")
    tn.write("exit\n")
    print tn.read_all()
    tn.close()


def set_config_file():
    paths = []
    selected_ip = raw_input("Ingresa la IP que del router que deseas restaurar: ")
    path = os.getcwd()
    r = selected_ip.replace(".", "-")
    directory = path + "/files/" + r
    paths.append(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
        make_connection(selected_ip, directory)
