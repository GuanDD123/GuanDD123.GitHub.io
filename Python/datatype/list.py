from array import array
from collections import deque
from typing import Iterable, Any
from _typeshed import SupportsRead, SupportsWrite


def _():
    [e for e in Iterable]
    [e for e in Iterable if ...]
    [(e1, e2) for e1 in Iterable for e2 in Iterable]

    (e for e in Iterable)
    (e for e in Iterable if ...)
    ((e1, e2) for e1 in Iterable for e2 in Iterable)

    deque(
        iterable=Iterable,
        maxlen=int)  # 设置最大长度，每加入一个元素的同时会删除最先一个元素

    array('b' | ...,
          Iterable)
    '''类型代码及对应的C存储类型
    b：signed char
    B：unsigned char
    h：signed short
    H：unsigned short
    i：signed int
    I：unsigned int
    l：signed long
    L：unsigned int
    f：float
    d：double
    '''

    range(int('stop'))
    range(int('start'), int('stop'),
          int('step'))


def max_min():
    max(...)
    min(...)

    max(list | tuple,  # 若 list 为空，引发 ValueError
        default=Any)  # 若 list 为空，返回 default


def length():
    len(list | tuple)


def copy_(L: list):
    L.copy()


def array_method(A: array):
    A.itemsize  # 返回单个元素的字节数
    A.typecode  # 返回在创建数组时使用的类型码字符

    A.tobytes()
    A.tofile(SupportsWrite[bytes])

    A.tolist()


def slice_(LTR: list | tuple | range):
    LTR[:]
    LTR[int('start'):] == LTR[slice(int('start'))]
    LTR[int('start'): int('stop')] == LTR[slice(int('start'), int('stop'))]
    LTR[int('start'): int('stop'): int('step')] == LTR[slice(int('start'), int('stop'), int('step'))]


def logic_judge():
    all(list | tuple | range)
    any(list | tuple | range)


def order():
    ord(str)  # 返回 unicode 顺序值
    chr(int)  # 返回 unicode 字符


def sort_(L: list, D: deque):
    L.reverse()
    reversed(list | tuple | range)

    L.sort(
        reverse=True,
        key=str.lower | len | ...)  # 从每个元素中提取比较键
    sorted(list | tuple | range,
           reverse=False,
           key=str.lower | len | ...)  # 从每个元素提取用于比较的键

    D.rotate(int)  # 向右循环移动 int 步；如果 int<0，向左循环


def concatenate(L: list, LT: list | tuple, D: deque):
    LT + LT
    L += L
    LT * int == int * LT

    L[int: int] = Iterable
    L.extend(Iterable)
    D.extendleft(Iterable)


def unpack(LTR: list | tuple | range, T: tuple):
    *LTR, Any, ...  # 返回一个元组

    '%s%s' % T  # 需 len(tuple) == 2

    var1, var2 = LTR
    var1, *var2 = LTR
    * var1, var2 = LTR

    var1, var2 = var2, var1


def select_elem(V: Any, LTR: list | tuple | range):
    ... in ...
    ... not in ...
    V in LTR

    LTR.index(Any)
    LTR.index(Any, int('start'),
              int('stop'))

    LTR.count(Any)


def add_elem(L: list, A: array):
    L.append(Any)
    L.insert(int, Any)

    A.frombytes(bytes)  # 将 bytes 转换为由机器值，添加到数组末尾
    A.fromfile(SupportsRead[bytes], int)  # 从文件对象中读取 int 项（视为机器值），添加到数组末尾；如果可用的项少于 int 项，引发 EOFError，但可用的项仍然会被加进数组
    A.fromlist(list[int])  # 将 list 中元素添加到数组末尾


def delete_elem(L: list, D: deque):
    L.clear()

    L.pop(
        int)
    del L[int: int: int]

    L.remove(Any)  # 若不存在元素 Any，引发 ValueError

    D.popleft()  # 若没有元素，引发IndexError
