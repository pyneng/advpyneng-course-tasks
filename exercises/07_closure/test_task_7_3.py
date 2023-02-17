import pytest
import task_7_3
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что функция создана"""
    check_function_exists(task_7_3, "get_item")


def test_get_item_returns_callable():
    last = task_7_3.get_item(-1)
    assert callable(last), "get_item должен возвращать вызываемый объект"


def test_get_item_last():
    data = [[1, 10, 100], [2, 20, 200]]
    last = task_7_3.get_item(-1)
    assert last(data) == [2, 20, 200], "Возвращается неправильное значение"


def test_get_item_name():
    data = {"name": "London1", "location": "London Str", "ip": "10.1.1.1"}
    get_name = task_7_3.get_item("name")
    assert get_name(data) == "London1", "Возвращается неправильное значение"


def test_get_item_sorted():
    data = [[20, 2, 200], [300, 3, 30], [1, 10, 100]]
    last = task_7_3.get_item(-1)
    assert sorted(data, key=last) == [[300, 3, 30], [1, 10, 100], [20, 2, 200]], "Возвращается неправильное значение"
