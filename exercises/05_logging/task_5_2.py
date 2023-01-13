# -*- coding: utf-8 -*-
"""
Задание 5.2

В файле cisco_ssh_class.py создан класс CiscoSSH и в классе есть log-сообщения.

Настроить логирование в задании таким образом, чтобы при выполнени кода в блоке
if __name__ == "__main__": был такой вывод:

$ python task_5_2.py
10:18:57 - cisco_ssh_class - DEBUG - SSH подключение к 192.168.139.1
10:18:58 - cisco_ssh_class - DEBUG - Отправка команды sh clock на 192.168.139.1
sh clock
*10:19:43.886 UTC Fri Sep 29 2022
R1#

При этом нельзя менять код в файле cisco_ssh_class.py.

Для заданий этого раздела нет тестов.
"""
from cisco_ssh_class import CiscoSSH


if __name__ == "__main__":
    r1 = CiscoSSH(
        "192.168.139.1", username="cisco", password="cisco", enable_password="cisco"
    )
    print(r1.send_show_command("sh clock"))
