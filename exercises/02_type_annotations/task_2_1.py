# -*- coding: utf-8 -*-
"""
Задание 2.1

Написать аннотацию для всех методов класса IPv4Network:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.
Тестом для этого раздела является mypy, после добавления аннотации mypy должен
отрабатывать без ошибок для данного кода, как минимум, в варианте запуска
mypy task_2_*.py (после добавления аннотации), а в идеале также и с добавлением --strict:
mypy task_2_*.py --strict
"""
import ipaddress


class IPv4Network:
    def __init__(self, network):
        self.network = network
        address, mask = network.split("/")
        self.network_address = address
        self.mask = int(mask)
        self.bin_mask = "1" * self.mask + "0" * (32 - self.mask)

    def hosts(self):
        net = ipaddress.ip_network(self.network)
        return [str(ip) for ip in net.hosts()]

    def __repr__(self):
        return f"Network('{self.network}')"

    def __len__(self):
        return len(self.hosts())

    def __iter__(self):
        return iter(self.hosts())


if __name__ == "__main__":
    net1 = IPv4Network("10.1.1.0/28")
    all_hosts = net1.hosts()
    print(all_hosts)
