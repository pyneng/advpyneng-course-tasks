import click
from click.testing import CliRunner
from task_4_2a import cli
import sys

sys.path.append("..")

from advpyneng_helper_functions import read_all_csv_content_as_list

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")


def test_cli(first_router_from_devices_yaml):
    host = first_router_from_devices_yaml["host"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    secret = first_router_from_devices_yaml["secret"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", host, "-u", username, "-p", password, "-s", secret],
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {host} -u {username} -p {password} -s {secret}'


def test_cli_input_secret(first_router_from_devices_yaml):
    host = first_router_from_devices_yaml["host"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    secret = first_router_from_devices_yaml["secret"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", host, "-u", username, "-p", password],
        input=secret,
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {host} -u {username} -p {password}'


def test_cli_input_username(first_router_from_devices_yaml):
    host = first_router_from_devices_yaml["host"]
    username = first_router_from_devices_yaml["username"]
    password = first_router_from_devices_yaml["password"]
    secret = first_router_from_devices_yaml["secret"]

    assert isinstance(
        cli, click.core.Command
    ), "Не настроен click. Декораторы click надо применять к функции cli"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["sh clock", host, "-p", password, "-s", secret],
        input=username,
    )
    assert (
        result.exit_code == 0
    ), f'CLI не отработал с таким вызовом python task_4_2a.py "sh clock" {host} -u {username} -p {password}'
