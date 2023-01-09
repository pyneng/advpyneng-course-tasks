# -*- coding: utf-8 -*-
"""
Задание 1.2a

Написать тест или тесты для функции convert_mac_list.

Функция convert_mac_list конвертирует список MAC-адресов из разных форматов в
1a:1b:2c:2d:3e:3f.

Если все MAC-адреса правильные, функция должна вернуть список этих же
MAC-адресов, но в формате 1a:1b:2c:2d:3e:3f. Если какие-то MAC-адреса
неправильные (функция convert_mac сгенерировала исключение ValueError), в
зависимости от параметра strict:
* strict равен True - генерируется исключение ValueError
* strict равен False - неправильные MAC-адреса игнорируются и в список
  добавляются только те, которые прошли проверку

Тест должен проверять работу функции для поддерживаемых форматов и для
неправильных данных. Примеры вызова функции написаны в коде задания.

Тест(ы) написать в файле заданий.

Ограничение: функцию менять нельзя.
Для заданий этого раздела нет тестов для проверки тестов.
"""
from pprint import pprint
from task_1_2 import convert_mac


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
    mac_list1 = ["1a1b.2c2d.3e3f", "111122223333", "11-11-22-22-33-33"]
    mac_list2 = ["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"]
    pprint(convert_mac_list(mac_list1, strict=False))
    pprint(convert_mac_list(mac_list2, strict=False))
    # errors
    try:
        pprint(convert_mac_list(mac_list2, strict=True))
    except ValueError as error:
        print(error)
