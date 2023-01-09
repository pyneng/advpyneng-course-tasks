# -*- coding: utf-8 -*-
"""
Задание 1.2a

Написать тест или тесты для функции convert_mac_list.

Функция convert_mac конвертирует mac-адрес из разных форматов в формат 1a:1b:2c:2d:3e:3f.
Должна поддерживаться конвертация из таких форматов:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a1b-2c2d-3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a:1b:2c:2d:3e:3f (оставить без изменений)

Если как аргумент была передана строка, которая не содержит правильный
MAC-адрес, функция генерирует исключение ValueError.

Тест должен проверять работу функции для поддерживаемых форматов и для
неправильных данных. Примеры вызова функции написаны в коде задания.

Тест(ы) написать в файле заданий.

Ограничение: функцию менять нельзя.
Для заданий этого раздела нет тестов для проверки тестов.
"""
from pprint import pprint
import re


def convert_mac(mac_address):
    regex = re.compile(
        r"[0-9a-f]{4}[.:-][0-9a-f]{4}[.:-][0-9a-f]{4}"
        r"|([0-9a-f]{2}[.:-]){5}[0-9a-f]{2}"
        r"|[0-9a-f]{12}"
    )
    if regex.fullmatch(str(mac_address)):
        mac = re.sub(r"[-.:]", "", mac_address)
    else:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    new_mac = [mac[index : index + 2] for index in range(0, len(mac), 2)]
    return ":".join(new_mac)


if __name__ == "__main__":
    pprint(convert_mac("1a1b.2c2d.3e3f"))
    pprint(convert_mac("111122223333"))
    pprint(convert_mac("1111-2222-3333"))
    # errors
    try:
        pprint(convert_mac("1111-2222-33"))
    except ValueError as error:
        print(error)
    try:
        pprint(convert_mac("1111-2222-33WW"))
    except ValueError as error:
        print(error)
