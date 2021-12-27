import socket
import threading
from datetime import datetime

from requests import head

start = datetime.now()  # для проверки времени отработки кода

http_port = {}  # тут храним название службы на портах 80, 443


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((ip, port))
        print('Port :', port, ' its open.')
        sock.close()
        if port in (80, 443):
            response = head(f'http://{ip}:{port}')
            if 'Server' in response.headers:
                http_port[(ip, port)] = response.headers['Server']
    except:
        pass


ip = '192.168.1.0/24'  # ip адресс, для проверки использовал свой
for i in range(1000):   # проверяю порты в диапазоне с 1 по 1000
    potoc = threading.Thread(target=scan_port, args=(ip, i))
    potoc.start()
    potoc.join()
ends = datetime.now()
print('Time : {}'.format(ends - start))
