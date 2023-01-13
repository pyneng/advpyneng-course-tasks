import pytest
import task_12_5
import sys

sys.path.append("..")

from advpyneng_helper_functions import check_class_exists, check_attr_or_method

# Проверка что тест вызван через pytest ..., а не python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Тесты нужно вызывать используя такое выражение:\npytest {__file__}\n\n")



def test_class_created():
    check_class_exists(task_12_5, "InheritanceMixin")


def test_mixin_class():
    class ForTest(task_12_5.InheritanceMixin):
        pass

    ins = ForTest()
    check_attr_or_method(ins, method="subclasses")
    check_attr_or_method(ins, method="superclasses")
    assert ForTest.superclasses() == [ForTest, task_12_5.InheritanceMixin, object]
    assert ForTest.subclasses() == []


def test_mixin_instance():
    class ForTest(task_12_5.InheritanceMixin):
        pass

    ins = ForTest()
    check_attr_or_method(ins, method="subclasses")
    check_attr_or_method(ins, method="superclasses")
    assert ins.superclasses() == [ForTest, task_12_5.InheritanceMixin, object]
    assert ins.subclasses() == []


def test_mixin_class():
    class ForTest(task_12_5.InheritanceMixin):
        pass

    class ChildForTest(ForTest):
        pass

    c_ins = ChildForTest()
    check_attr_or_method(c_ins, method="subclasses")
    check_attr_or_method(c_ins, method="superclasses")
    assert ForTest.subclasses() == [ChildForTest]
