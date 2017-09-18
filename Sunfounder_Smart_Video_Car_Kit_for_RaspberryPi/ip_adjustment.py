import socket
import os


def get_ip_addr():
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

if __name__ == "__main__":
    cwd_name = parse_cwd_name()
    if parse_cwd_name() != expected_cwd:
        print("Error : 디렉토리 오류 \nError Message : " + expected_cwd + " 폴더에서 실행해야 합니다.")
    else:
        print("작업이 시작되었습니다")
        ip = get_ip_addr()
        print("이 컴퓨터의 ip 주소 감지 : %s" % ip)
        for file in files:
            with open(file, "r+") as f:
                print(f.read())
