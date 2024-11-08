from typing import Iterable, Any


def length():
    len(set | frozenset)


def copy_(S: set):
    S.copy()


def basic_operate(S: set, SF: set | frozenset):
    SF & SF  # 交集运算
    SF.intersection(Iterable, ...)
    S.intersection_update(Iterable, ...)  # 同时更新 set

    SF | SF  # 并集运算
    SF.union(Iterable, ...)
    S.update(Iterable, ...)

    SF - SF  # 差集运算
    SF.difference(Iterable, ...)
    S.difference_update(Iterable, ...)

    SF ^ SF  # 异或运算（对称差）
    SF.symmetric_difference(Iterable, ...)
    S.symmetric_difference_update(Iterable, ...)


def judge_set(SF: set | frozenset):
    SF.isdisjoint(Iterable)  # 若 set 中没有与 Iterable 共有的元素，则返回 True

    SF <= SF
    SF.issubset(Iterable)  # 若 set 中每个元素都在 Iterable 中，则返回 True
    SF < SF

    SF >= SF
    SF.issuperset(Iterable)  # 若 Iterable 中每个元素都在 set 中，则返回 True
    SF > SF


def select_elem(value: Any, SF: set | frozenset):
    ... in ...
    ... not in ...
    value in SF


def add_elem(S: set):
    S.add(Any)


def delete_elem(S: set):
    S.clear()

    S.pop()  # 返回 set 中第一个元素，并将其从 set 中移除

    S.discard(Any)
    S.remove(Any)  # 若不存在元素 Any，引发 KeyError
