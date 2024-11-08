from _collections_abc import dict_keys, dict_values, dict_items
from types import MappingProxyType
from typing import Iterable, Any


def _():
    {key: value for key, value in Iterable}
    {key: value for value, key in Iterable}
    {key: value for key, value in Iterable if ...}

    dict.fromkeys(Iterable,  # 使用 iterable 的键创建字典
                  Any)  # 设置键值为 Any（默认为 None）

    vars(  # 更新并返回表示当前本地符号表的字典；
        # 在函数块中调用时，将返回自由变量，但在类块中则不会返回；
        # 在模块级别，locals() 和 globals() 是同一个字典
        object)  # 返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性
    globals()  # 返回包含全局变量的字典
    locals()  # 返回包含局部变量的字典


def length():
    len(dict | MappingProxyType)


def copy_(D: dict):
    D.copy()


def get_view(DM: dict | MappingProxyType):
    list(dict | MappingProxyType | dict_values | dict_items)
    iter(dict | MappingProxyType | dict_values | dict_items)

    DM.keys()
    DM.values()
    DM.items()


def mapping(K: dict_keys, V: dict_values, I: dict_items):
    K.mapping == V.mapping == I.mapping  # 返回封装了原始字典的 types.MappingProxyType 对象


def sort_():
    reversed(dict | MappingProxyType | dict_values | dict_items)

    sorted(dict | MappingProxyType | dict_values | dict_items,
           reverse=True,
           key=lambda d: d[1],
           key=lambda d: (d[1], d[0]))


def concatenate(D: dict, DM: dict | MappingProxyType, DM_2: dict | MappingProxyType):
    DM | DM_2   # 返回一个字典，元素为 DM 与 DM_2 中元素值，DM_2 会覆盖 DM 的键
    {**DM, **DM_2}
    D.update(dict)


def unpack(DM: dict | MappingProxyType, DM_2: dict | MappingProxyType):
    {**DM, **DM_2}
    {**DM, Any: Any}


def select_value(D: dict, DM: dict | MappingProxyType, A: Any,
                 DMK: dict | MappingProxyType | dict_keys, I: dict_items):
    ... in ...
    ... not in ...
    A in DMK
    (A, A) in I

    DM.get(Any('key'),
           Any('default'))  # 若不存在 key，则返回 default（默认返回 None）
    D.setdefault(Any('key'),  # 返回 key 对应的值；若不存在 Any，则插入值为 None 的键 key
                 Any('default'))  # 若不存在 key，则插入值为 default 的键 key


def delete_item(D: dict):
    D.clear()

    D.pop(Any('key'),  # 未找到 key，引发 KeyError
          Any('default'))  # 未找到 key，返回 default
    del D[Any('key')]  # 若不存在键 Any，引发 KeyError

    D.popitem()  # 随机弹出一个项
