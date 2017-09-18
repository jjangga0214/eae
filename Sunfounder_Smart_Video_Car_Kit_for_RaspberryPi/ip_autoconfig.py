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


file_paths = ["./server/cali_server.py",
              "./server/tcp_server.py",
              "./client/cali_client.py",
              "./client/client_App.py"]

expected_cwd = "Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi"


def ip_autoconfig():
    cwd_name = parse_cwd_name()
    if parse_cwd_name() != expected_cwd:
        print("현재 이 파이썬 파일이 위치한 디렉토리의 이름이 %s 가 아닌 %s 입니다." % (expected_cwd, cwd_name))
        while True:
            response = input("계속 작업할까요? [y/n] : ").strip().lower()

            if response == "y":
                break
            elif response == "n":
                print("아무런 작업이 실행되지 않은채로 종료합니다")
                return
            else:
                print("응답으로는 y 또는 n 을 입력해주세요")

    try:
        ip = get_ip_addr()
        print("이 컴퓨터의 ip 주소 감지 : %s" % ip)
    except socket.gaierror:
        print("인터넷에 연결되어 있지 않은 것 같습니다. 자동으로 ip를 찾을 수 없습니다.")
        while True:
            response = input("로컬 네트워크로 연결된 경우, 수동으로 ip를 입력하시겠습니다. ? [y/n] : ")

            if response == "y":
                ip = input("ip : ").strip()
                break
            elif response == "n":
                print("아무런 작업이 실행되지 않은채로 종료합니다")
                return
            else:
                print("응답으로는 y 또는 n 을 입력해주세요")
    print("작업이 시작되었습니다")
    for file_path in file_paths:
        try:
            with open(file_path, "r+") as f:
                new_lines = []
                for line in f:
                    if line.startswith("HOST"):
                        line = "HOST = \'%s\'\n" % ip
                    new_lines.append(line)
                f.seek(0)
                f.writelines(new_lines)

                print(file_path + " 작업 완료..")
        except FileNotFoundError:
            print("[경고!] " + file_path + " 를 찾을 수 없습니다. 해당 파일에 대해서는 작업을 수행하지 않습니다.")

    print("작업이 완료되었습니다. 모든 HOST 변수의 값이 \'%s\' 로 변경되었습니다." % ip)


if __name__ == "__main__":
    ip_autoconfig()
