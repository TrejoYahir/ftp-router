from configuration import Configuration
from get_config import get_config_file
from set_config import set_config_file
import time


def config(network):
    cont = 0
    for ip in network.get_ip_list():
        print(network.get_path(cont), ip)
        get_config_file(network.get_path(cont), ip)
        cont += 1
        time.sleep(2)


def set_paths():
    ip_list = []
    # Get ip list
    with open("networks.txt") as ips:
        for ip in ips:
            ip_list.append(ip.replace("\n", ""))
    # Create ip folders and get config files
    network = Configuration(ip_list)
    config(network)


def main():
    opc = 0
    while opc < 3:
        print "\nSeleccionar opcion:\n 1. Respaldar configuraciones \n 2. Restaurar configuracion\n 3. Salir"
        opc = input(">> ")
        if opc == 1:
            set_paths()
        elif opc == 2:
            set_config_file()
        else:
            exit()


main()
