import platform
import time
from datetime import datetime as dt

win_hosts_path = r'/c/Windows/System32/Drivers/etc/hosts'
osx_linux_hosts_path = r'etc/hosts'

temp_path = r'hosts'

redirect = '127.0.0.1'
websites = ['www.example.com', 'example.com']

if (platform.system() == 'Windows'):
    hosts_path = win_hosts_path
else:
    hosts_path = osx_linux_hosts_path

hosts_path = temp_path

while True:
    if 9 < dt.now().hour < 18:
        print('Working hour')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print('Off hour')
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(10)
