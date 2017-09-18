창연공 util 프로젝트
=====================

라즈베리 파이 HOST 자동 설정하기
---------------------------
라즈베리 파이로 구동체를 켈리브레이션하고, 움직이기 위해서는 `Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi` 폴더 안의 4개 파일에 대해 HOST 변수를 라즈베리 파이의 ip 로 설정해야합니다. 해당 4개 파일은 다음과 같습니다.

* `server/cali_server.py`
* `server/tcp_server.py`
* `client/cali_client.py`
* `client/client_App.py`

직접 라즈베리 파이에서 `ifconfig` 를 통해 `ip`를 알아내어, 위의 4개 파일의 `HOST` 변수의 값을 설정하는 것은 매우 성가신 일입니다. 더 심각한 것은 와이파이, 또는 랜선으로 연결된 이더넷이 변경될 때마다 이 설정을 하나하나 다시 해주어야 한다는 것입니다. 집, 작업공간, 강의실을 오고가며 와이파이가 매번 바뀌기 때문에, 이는 자동화될 필요가 있습니다. **빠르고 손쉽게, `ip`를 자동으로 인식해 설정하는 조그마한 프로그램을 작성했고, 혹여 도움을 받으실 분이 있을까 하는 생각에 공유하려 합니다.**

#### 설치
터미널에서 라즈베리 파이의 `Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi` 폴더 안으로 이동한 후, 다음 명령어를 입력해 python 파일을 해당 폴더에 다운로드 받습니다. 만일 해당 폴더의 이름을 바꾸었더라도, 어쨌든 `server` 폴더와 `client` 폴더가 있다면 이름은 꼭 `Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi` 가 아니어도 괜찮습니다.
```shell
sudo wget -O ip_autoconfig.py https://goo.gl/C57Gpa
```

#### 동작
설치 후에는 다음과 같이 간단하게 다운로드 받은 파이썬 파일을 실행하면 됩니다. 자동으로 `ip`를 추출하여 모든 설정을 자동으로 해줄 것입니다. 만일 네트워크에 연결되지 않았다면 `ip`를 수동으로 입력받습니다. 단, 이 파일은 python 3로 작성되었기 때문에, **python3 명령어를 사용해서 실행해주세요.**
```shell
sudo python3 ip_autoconfig.py
```
