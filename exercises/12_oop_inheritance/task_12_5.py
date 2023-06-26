# -*- coding: utf-8 -*-
"""
Задание 12.5

Создать примесь InheritanceMixin с двумя методами:

* subclasses - отображает дочерние классы
* superclasses - отображает родительские классы

Методы должны возвращать именно списки классов, не имена классов как строки.

Методы должны отрабатывать и при вызове через класс и при вызове
через экземпляр:

In [1]: from task_12_5 import A, B, C, D, E

In [2]: A.superclasses()
Out[2]: [task_12_5.A, task_12_5.InheritanceMixin, object]

In [4]: A.subclasses()
Out[4]: [task_12_5.B, task_12_5.D]

In [5]: a = A()

In [6]: a.superclasses()
Out[6]: [task_12_5.A, task_12_5.InheritanceMixin, object]

In [7]: a.subclasses()
Out[7]: [task_12_5.B, task_12_5.D]

In [8]: D.superclasses()
Out[8]: [task_12_5.D, task_12_5.A, task_12_5.C, task_12_5.InheritanceMixin, object]

In [9]: D.subclasses()
Out[9]: []


В задании заготовлена иерархия классов, надо сделать так, чтобы у всех
этих классов повились методы subclasses и superclasses.
Определение классов можно менять.
"""


class InheritanceMixin:
    pass


class A(InheritanceMixin):
    pass


class B(A):
    pass


class E(B):
    pass


class C(InheritanceMixin):
    pass


class D(A, C):
    pass
