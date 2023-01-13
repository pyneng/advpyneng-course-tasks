# -*- coding: utf-8 -*-
"""
Задание 2.4

Написать аннотацию для функций convert_mac и convert_mac_list:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.

Тестом для этого раздела является mypy, после добавления аннотации mypy должен
отрабатывать без ошибок для данного кода, как минимум, в варианте запуска
mypy task_2_*.py, а в идеале также и с добавлением --strict: mypy task_2_*.py --strict
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


def convert_mac_list(mac_list, strict=False):
    converted_mac_list = []
    for mac in mac_list:
        try:
            new_mac = convert_mac(mac)
        except ValueError:
            if strict:
                raise
        else:
            converted_mac_list.append(new_mac)
    return converted_mac_list


if __name__ == "__main__":
    # вызов convert_mac
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

    # вызов convert_mac_list
    mac_list1 = ["1a1b.2c2d.3e3f", "111122223333", "11-11-22-22-33-33"]
    mac_list2 = ["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"]
    pprint(convert_mac_list(mac_list1, strict=False))
    pprint(convert_mac_list(mac_list2, strict=False))
    # errors
    try:
        pprint(convert_mac_list(mac_list2, strict=True))
    except ValueError as error:
        print(error)
