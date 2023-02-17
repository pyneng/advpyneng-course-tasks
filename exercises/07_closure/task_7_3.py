# -*- coding: utf-8 -*-
"""
Задание 7.3

Переделать функцию netmiko_ssh таким образом, чтобы при отправке строки "close",
вместо отправки "close" как команды на оборудование, закрывалось соединение к устройству
и выводилось сообщение 'Соединение закрыто'.

Пример работы функции:

In [4]: sorted(list_of_tuples, key=get_item(1))
Out[4]: [('DB_VLAN', 11), ('Mngmt_VLAN', 99), ('IT_VLAN', 320), ('User_VLAN', 1010)]

In [5]: pprint(sorted(data, key=get_item("ip")))
[{'interface': 'Gi0/2', 'ip': '10.0.12.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/3', 'ip': '10.0.13.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/1', 'ip': '10.0.15.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/4', 'ip': '10.0.17.1', 'protocol': 'up', 'status': 'up'}]

In [6]: pprint(sorted(data, key=get_item("interface")))
[{'interface': 'Gi0/1', 'ip': '10.0.15.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/2', 'ip': '10.0.12.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/3', 'ip': '10.0.13.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/4', 'ip': '10.0.17.1', 'protocol': 'up', 'status': 'up'}]

"""
from pprint import pprint

list_of_tuples = [
    ("IT_VLAN", 320),
    ("Mngmt_VLAN", 99),
    ("User_VLAN", 1010),
    ("DB_VLAN", 11),
]

data = [
    {"interface": "Gi0/3", "ip": "10.0.13.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/2", "ip": "10.0.12.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/4", "ip": "10.0.17.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/1", "ip": "10.0.15.1", "status": "up", "protocol": "up"},
]
