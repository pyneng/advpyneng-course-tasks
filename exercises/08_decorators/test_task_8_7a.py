import time
import pytest
import task_8_7a
import logging
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_function_exists, check_function_params


# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_func_created():
    """Проверяем, что декоратор создан"""
    check_function_exists(task_8_7a, "print_to_log")


def test_print_to_log_one_print(capsys):
    logging.basicConfig(
        level=logging.INFO, format="{name} {levelname} {message}", style="{", force=True
    )

    @task_8_7a.print_to_log
    def do_thing(a, b):
        print(f"args: {a} {b}")
        return a + b

    return_value = do_thing("A", "B")
    # проверка базовой работы функции
    assert return_value == "AB"

    # на stderr должно выводиться log-сообщение
    correct_stderr = "root info args: a b"
    err = capsys.readouterr().err
    assert err != "", "На stderr не выведена информация"
    assert correct_stderr in err.lower(), "На stderr должно выводиться сообщение"


def test_print_to_log_multiple_str_args(capsys):
    logging.basicConfig(
        level=logging.INFO, format="{name} {levelname} {message}", style="{", force=True
    )

    @task_8_7a.print_to_log
    def dummy(a, b, c):
        print(a, b, c)
        return f"{a} {b} {c}"

    return_value = dummy("python", "ruby", "perl")
    # проверка базовой работы функции
    assert return_value == "python ruby perl"

    # на stderr должны выводиться log-сообщения
    correct_stderr = "root info python ruby perl"
    err = capsys.readouterr().err
    assert err != "", "На stderr не выведена информация"
    assert correct_stderr in err.lower(), "На stderr должно выводиться сообщение"
    # проверка, что print работает как обычно
    test_line = "test line 42"
    print(test_line)
    out = capsys.readouterr().out
    assert (
        test_line in out.lower()
    ), "print должен работать как обычно после вызове декорируемой функции"


def test_print_to_log_multiple_int_args(capsys):
    logging.basicConfig(
        level=logging.INFO, format="{name} {levelname} {message}", style="{", force=True
    )

    @task_8_7a.print_to_log
    def dummy(a, b, c):
        print(a, b, c)
        return f"{a} {b} {c}"

    return_value = dummy(10, 20, 42)
    # проверка базовой работы функции
    assert return_value == "10 20 42"

    # на stderr должны выводиться log-сообщения
    correct_stderr = "root info 10 20 42"
    err = capsys.readouterr().err
    assert err != "", "На stderr не выведена информация"
    assert correct_stderr in err.lower(), "На stderr должно выводиться сообщение"


def test_print_to_log_multiple_args_sep(capsys):
    logging.basicConfig(
        level=logging.INFO, format="{name} {levelname} {message}", style="{", force=True
    )

    @task_8_7a.print_to_log
    def dummy(a, b, c):
        print(a, b, c, sep=" | ")
        return f"{a} {b} {c}"

    return_value = dummy(10, 20, 42)
    # проверка базовой работы функции
    assert return_value == "10 20 42"

    # на stderr должны выводиться log-сообщения
    correct_stderr = "root info 10 | 20 | 42"
    err = capsys.readouterr().err
    assert err != "", "На stderr не выведена информация"
    assert correct_stderr in err.lower(), "На stderr должно выводиться сообщение"
