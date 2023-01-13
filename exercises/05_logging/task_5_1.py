# -*- coding: utf-8 -*-
"""
Задание 5.1

Добавить логирование в скрипт с выводом информации на стандартный поток вывода.
Формат логов и сообщения надо определить из примеров вывода ниже. Кроме того,
это должен быть единственный вывод модуля logging, сообщения других модулей
надо выводить только если их уровень WARNING.


Пример вывода при успешном подключении на все три устройства:
$ python task_5_1.py
ThreadPoolExecutor-0_0 2023-01-13 17:11:02,385 root DEBUG: Подключение к 192.168.139.1
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,392 root DEBUG: Подключение к 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,394 root DEBUG: Подключение к 192.168.139.3
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,686 root DEBUG: Получен ответ от 192.168.139.2
ThreadPoolExecutor-0_0 2023-01-13 17:11:02,762 root DEBUG: Получен ответ от 192.168.139.1
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,857 root DEBUG: Получен ответ от 192.168.139.3
{'192.168.139.1': '*17:07:17.869 UTC Fri Jan 13 2023',
 '192.168.139.2': '*17:07:17.832 UTC Fri Jan 13 2023',
 '192.168.139.3': '*17:07:17.833 UTC Fri Jan 13 2023'}


Пример вывода при ошибке аутентификации на первом устройстве (неправильный пароль):
$ python task_5_1.py
ThreadPoolExecutor-0_0 2023-01-13 17:11:02,867 root DEBUG: Подключение к 192.168.139.1
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,875 root DEBUG: Подключение к 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,878 root DEBUG: Подключение к 192.168.139.3
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,138 root DEBUG: Получен ответ от 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,252 root DEBUG: Получен ответ от 192.168.139.3
ThreadPoolExecutor-0_0 2023-01-13 17:11:44,179 root WARNING: Authentication to device failed.

Common causes of this problem are:
1. Invalid username and password
2. Incorrect SSH-key file
3. Connecting to the wrong device

Device settings: cisco_ios 192.168.139.1:22


Authentication failed.
{'192.168.139.1': NetmikoAuthenticationException('Authentication to device failed.\n\nCommon causes of this problem ar
e:\n1. Invalid username and password\n2. Incorrect SSH-key file\n3. Connecting to the wrong device\n\nDevice settings:
 cisco_ios 192.168.139.1:22\n\n\nAuthentication failed.'),
 '192.168.139.2': '*17:08:43.018 UTC Fri Jan 13 2023',
 '192.168.139.3': '*17:08:43.009 UTC Fri Jan 13 2023'}


Пример вывода при ошибке перехода в enable на первом устройстве (неправильный пароль на enable):
$ python task_5_1.py
ThreadPoolExecutor-0_0 2023-01-13 17:11:02,096 root DEBUG: Подключение к 192.168.139.1
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,102 root DEBUG: Подключение к 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,104 root DEBUG: Подключение к 192.168.139.3
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,462 root DEBUG: Получен ответ от 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,589 root DEBUG: Получен ответ от 192.168.139.3
ThreadPoolExecutor-0_0 2023-01-13 17:11:38,736 root WARNING: Не получилось перейти в режим enable
{'192.168.139.1': ReadTimeout("\n\nPattern not detected: 'R1' in output.\n\nThings you might try to fix this:\n1. Adju
st the regex pattern to better identify the terminating string. Note, in\nmany situations the pattern is automatically
 based on the network device's prompt.\n2. Increase the read_timeout to a larger value.\n\nYou can also look at the Ne
tmiko session_log or debug log for more information.\n\n"),
 '192.168.139.2': '*17:10:19.139 UTC Fri Jan 13 2023',
 '192.168.139.3': '*17:10:19.125 UTC Fri Jan 13 2023'}

Пример вывода при недоступном IP-адресе:
$ python task_5_1.py
ThreadPoolExecutor-0_0 2023-01-13 17:11:00,922 root DEBUG: Подключение к 192.168.139.13
ThreadPoolExecutor-0_1 2023-01-13 17:11:00,926 root DEBUG: Подключение к 192.168.139.2
ThreadPoolExecutor-0_2 2023-01-13 17:11:00,928 root DEBUG: Подключение к 192.168.139.3
ThreadPoolExecutor-0_2 2023-01-13 17:11:02,170 root DEBUG: Получен ответ от 192.168.139.3
ThreadPoolExecutor-0_1 2023-01-13 17:11:02,185 root DEBUG: Получен ответ от 192.168.139.2
ThreadPoolExecutor-0_0 2023-01-13 17:11:16,689 root WARNING: TCP connection to device failed.

Common causes of this problem are:
1. Incorrect hostname or IP address.
2. Wrong TCP port.
3. Intermediate firewall blocking access.

Device settings: cisco_ios 192.168.139.13:22


{'192.168.139.13': NetmikoTimeoutException('TCP connection to device failed.\n\nCommon causes of this problem are:\n1.
 Incorrect hostname or IP address.\n2. Wrong TCP port.\n3. Intermediate firewall blocking access.\n\nDevice settings:
cisco_ios 192.168.139.13:22\n\n'),
 '192.168.139.2': '*17:11:07.731 UTC Fri Jan 13 2023',
 '192.168.139.3': '*17:11:07.585 UTC Fri Jan 13 2023'}


Для заданий этого раздела нет тестов.
"""

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from itertools import repeat
import yaml
from netmiko import Netmiko
from netmiko.exceptions import SSHException, ReadTimeout


def send_show(device_dict, command):
    try:
        with Netmiko(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except SSHException as error:
        return error
    except ReadTimeout as error:
        return error


def send_command_to_devices(devices, command, max_workers=5):
    data = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    pprint(send_command_to_devices(devices, "sh clock"))
