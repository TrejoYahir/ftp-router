import os


class Configuration:

    def __init__(self, ip_list):

        path = os.getcwd()
        paths = []
        for r in ip_list:
            r = r.replace(".", "-")
            directory = path + "/files/" + r
            paths.append(directory)
            if not os.path.exists(directory):
                os.makedirs(directory)

        self.path = paths
        self.ip_list = ip_list

    def get_ip_list(self):
        return self.ip_list

    def get_path(self, cont):
        return self.path[cont]

