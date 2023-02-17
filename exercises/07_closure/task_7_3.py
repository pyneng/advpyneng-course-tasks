# -*- coding: utf-8 -*-
"""
Задание 7.3

Создать функцию get_item, которая возвращает функцию для получения указанного
элемента с помощью метода __getitem__ (вызов obj[item]).

У функции get_item должен быть один параметр item, который принимает как
аргумент индекс или ключ, который надо получить. Функция get_item возвращает
функцию: эта функция ожидает как аргумент объект и возвращает элемент
соответствующий указанному индексу или ключу item.

Например, с помощью функции get_item можно создать функцию для получения
первого или последнего элемента последовательности:

In [1]: first = get_item(0)

In [2]: first(vlans)
Out[2]: ('IT_VLAN', 320)

In [3]: first(intf_list)
Out[3]: {'interface': 'Gi0/3', 'ip': '10.0.13.1', 'status': 'up', 'protocol': 'up'}

In [4]: last = get_item(-1)

In [5]: last(vlans)
Out[5]: ('DB_VLAN', 11)

In [6]: last(intf_list)
Out[6]: {'interface': 'Gi0/1', 'ip': '10.0.15.1', 'status': 'up', 'protocol': 'up'}


Или функцию для получения значения конкретного ключа:

In [4]: get_ip = get_item("ip")

In [5]: get_ip(intf)
Out[5]: '10.0.13.1'

Эту же функцию можно использовать для сортировки:

In [6]: sorted(vlans, key=get_item(1))
Out[6]: [('DB_VLAN', 11), ('Mngmt_VLAN', 99), ('IT_VLAN', 320), ('User_VLAN', 1010)]

In [7]: pprint(sorted(intf_list, key=get_item("ip")))
[{'interface': 'Gi0/2', 'ip': '10.0.12.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/3', 'ip': '10.0.13.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/1', 'ip': '10.0.15.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/4', 'ip': '10.0.17.1', 'protocol': 'up', 'status': 'up'}]

In [8]: pprint(sorted(intf_list, key=get_item("interface")))
[{'interface': 'Gi0/1', 'ip': '10.0.15.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/2', 'ip': '10.0.12.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/3', 'ip': '10.0.13.1', 'protocol': 'up', 'status': 'up'},
 {'interface': 'Gi0/4', 'ip': '10.0.17.1', 'protocol': 'up', 'status': 'up'}]

"""
from pprint import pprint

vlans = [("IT_VLAN", 320), ("Mngmt_VLAN", 99), ("User_VLAN", 1010), ("DB_VLAN", 11)]
intf = {"interface": "Gi0/3", "ip": "10.0.13.1", "status": "up", "protocol": "up"}
intf_list = [
    {"interface": "Gi0/3", "ip": "10.0.13.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/2", "ip": "10.0.12.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/4", "ip": "10.0.17.1", "status": "up", "protocol": "up"},
    {"interface": "Gi0/1", "ip": "10.0.15.1", "status": "up", "protocol": "up"},
]
