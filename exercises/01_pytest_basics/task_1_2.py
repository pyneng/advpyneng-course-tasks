# -*- coding: utf-8 -*-
"""
Задание 1.2

Написать тест или тесты для функции get_int_vlan_map. Тест должен проверять,
что словари, которые возвращает функция, содержат правильные данные.

Пример вызова функции показан в файле заданий.

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
    if regex.fullmatch(mac_address):
        mac = re.sub(r"[-.:]", "", mac_address)
    else:
        raise ValueError(f"'{mac_address}' does not appear to be a MAC address")

    new_mac = [mac[index : index + 2] for index in range(0, len(mac), 2)]
    return ":".join(new_mac)


if __name__ == "__main__":
    pprint(convert_mac("1a1b.2c2d.3e3f"))
    pprint(convert_mac("1111.2222.3333"))
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


"""
Должна поддерживаться конвертация из таких форматов:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a1b-2c2d-3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a:1b:2c:2d:3e:3f (оставить без изменений)

Функция также должна проверять, что строка, которая была передана функции,
содержит правильный MAC-адрес. MAC-адрес считается правильным, если:
- каждый символ, кроме разделителей ":-.", это символ в диапазоне a-f или 0-9
- не считая разделители, в MAC-адресе должно быть 12 символов

Проверок выше достаточно для этого задания, то есть не обязательно проверять формат
адреса более точно.

Если как аргумент была передана строка, которая не содержит правильный
MAC-адрес, сгенерировать исключение ValueError (... должно быть заменено на
переданное значение, примеры ниже): ValueError: '...' does not appear to be a
MAC address
"""
