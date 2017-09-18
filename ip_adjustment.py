import socket
import os


def get_ipaddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    r = s.getsockname()[0]
    s.close()
    return r


def parse_cwd_name():
    cwd = os.getcwd()
    path_units = cwd.split("/")
    return path_units.pop()


files = ["./server/cali_server.py",
         "./server/tcp_server.py",
         "./client/cali_client.py",
         "./client/client_App.py"]

expected_cwd = "Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi"


