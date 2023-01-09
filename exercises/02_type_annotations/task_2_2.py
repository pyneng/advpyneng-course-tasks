# -*- coding: utf-8 -*-
"""
Задание 2.2

Написать аннотацию для функций send_show и send_command_to_devices:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.

Тестом для этого раздела является mypy, после добавления аннотации mypy должен
отрабатывать без ошибок для данного кода, как минимум, в варианте запуска
mypy task_2_*.py, а в идеале также и с добавлением --strict: mypy task_2_*.py --strict
"""
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from pprint import pprint

from netmiko import Netmiko
from netmiko.exceptions import SSHException
import yaml


def send_show(device_dict, command):
    try:
        with Netmiko(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except SSHException as error:
        return str(error)


def send_command_to_devices(devices, command, max_workers=3):
    data = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    pprint(send_command_to_devices(devices, "sh ip int br"))
