# -*- coding: utf-8 -*-
"""
Задание 8.7a

Скопировать декоратор print_to_log из задания 8.7.
Доработать его таким образом, чтобы он мог заменить print несколькими
аргументами и поддерживал print с указанным разделителем.
В задании созданы три функции с разными вызовами print (можно использовать их
как разные этапы задания):
* send_show_command - print с несколькими аргументами, все аргументы строки
* send_command_list - print с несколькими аргументами, некоторые аргументы не строки
* dummy - аргументы не строки и используется sep

Замена print выполняется только на время работы функции и не должна менять
функцию print глобально.

Декоратор должен работать с любой функцией.
Проверить работу декоратора на функциях send_show_command, send_command_list, dummy.

Пример вывода после декорации всех функций:
$ python task_8_7a.py
BEFORE
14:06:41 root INFO >>> Подключение r1
14:06:41 root INFO <<< Получен вывод sh clock с устройства r1
14:06:41 root INFO >>> Подключение r1
14:06:42 root INFO <<< Получен вывод ['sh clock', 'sh ip int br'] с устройства r1
14:06:42 root INFO 1|2|3
AFTER

"""
import time
import logging


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {name} {levelname} {message}",
    style="{",
    datefmt="%H:%M:%S",
)


def send_show_command(device, command):
    print(">>> Подключение", device)
    time.sleep(0.5)
    print("<<< Получен вывод", command, "с устройства", device)
    return f"{device} {command}"


def send_command_list(device, commands):
    print(">>> Подключение", device)
    time.sleep(0.5)
    print("<<< Получен вывод", commands, "с устройства", device)
    return f"{device} {commands}"


def dummy(items):
    print(*items, sep="|")


if __name__ == "__main__":
    print("BEFORE")
    result = send_show_command("r1", "sh clock")
    result = send_command_list("r1", ["sh clock", "sh ip int br"])
    dummy([1, 2, 3])
    print("AFTER")
