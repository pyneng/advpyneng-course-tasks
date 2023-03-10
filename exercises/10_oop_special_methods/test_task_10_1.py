import pytest
import task_10_1
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_class_created():
    """Проверяем, что класс создан"""
    check_class_exists(task_10_1, "IPv4Network")


def test_sequence_special_methods_created():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    check_attr_or_method(net, method="__getitem__")
    check_attr_or_method(net, method="__len__")
    check_attr_or_method(net, method="__contains__")
    check_attr_or_method(net, method="__iter__")
    check_attr_or_method(net, method="index")
    check_attr_or_method(net, method="count")


def test_sequence_special_methods_getitem():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert (
        net[1] == "100.7.1.2"
    ), "В сети 100.7.1.0/29 под индексом 1 должен находиться адрес 100.7.1.2"
    assert (
        net[-1] == "100.7.1.6"
    ), "В сети 100.7.1.0/29 под индексом -1 должен находиться адрес100.7.1.6"
    assert net[1:4] == (
        "100.7.1.2",
        "100.7.1.3",
        "100.7.1.4",
    ), "Срез [1:4] сети 100.7.1.0/29 должен возвращать кортеж с адресами ('100.7.1.2', '100.7.1.3', '100.7.1.4')"


def test_sequence_special_methods_len():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert len(net) == 6, "Для сети 100.7.1.0/29 количество хостов 6"


def test_sequence_special_methods_contains():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert "100.7.1.3" in net, "Должно возвращать True"
    assert "10.17.1.9" not in net, "Должно возвращать True"


def test_sequence_special_methods_iter():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    iterator = iter(net)
    assert (
        next(iterator) == "100.7.1.1"
    ), "Для сети 100.7.1.0/29 первым адресом должен быть 100.7.1.1"


def test_sequence_special_methods_index():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert net.index("100.7.1.4") == 3, "Для сети 100.7.1.0/29 index 100.7.1.4 равен 3"


def test_sequence_special_methods_count():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert (
        net.count("100.7.1.4") == 1
    ), "Адрес 100.7.1.4 входит в сеть 100.7.1.0/29 поэтому количество должно быть 1"
    assert (
        net.count("100.7.1.9") == 0
    ), "Адрес 100.7.1.4 не входит в сеть 100.7.1.0/29 поэтому количество должно быть 0"


def test_str():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert (
        str(net) == "100.7.1.0/29"
    ), "Неправильное cтроковое представление для сети 100.7.1.0/29"


def test_repr():
    net = task_10_1.IPv4Network("100.7.1.0/29")
    assert (
        repr(net) == "IPv4Network('100.7.1.0/29')"
    ), "Неправильное cтроковое представление для сети 100.7.1.0/29"
