# -*- coding: utf-8 -*-
"""
Задание 8.7

Создать декоратор print_to_log, который заменяет функцию print на logging.info
в декорируемой функции. Замена print выполняется только на время работы функции
и не должна менять функцию print глобально.

Декоратор должен работать с любой функцией.
Проверить работу декоратора на функции send_show_command.

Вывод до декорации функции send_show_command:
$ python task_8_7.py
BEFORE
>>> Подключение
<<< Получен вывод
AFTER


Пример вывода после декорации функции:
$ python task_8_7.py
BEFORE
13:56:40 root INFO >>> Подключение
13:56:41 root INFO <<< Получен вывод
AFTER

На данном этапе считаем, что надо заменить print, которому передается только
одна строка.  В следующем задании надо будет сделать поддержку нескольких
аргументов.

Подсказка: замену print надо делать через builtins.print
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
    print(">>> Подключение")
    time.sleep(1)
    print("<<< Получен вывод")
    return f"{device} {command}"


if __name__ == "__main__":
    print("BEFORE")
    result = send_show_command("r1", "sh clock")
    print("AFTER")
