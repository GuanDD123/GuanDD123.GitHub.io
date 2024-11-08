from typing import Iterable, Any


def zip_enum():
    zip(Iterable, ...)  # 返回元组的迭代器，其中第 i 个元组包含的是每个 iterable 的第 i 个元素
    enumerate(iterable=Iterable,  # 返回一个枚举对象，包含多个元组，每个元组包含一个计数值（从 0 开始）和迭代 iterable 获得的值
              start=int)  # 计数值从 start 开始


def type_object():
    type(object)
    isinstance(object, type)  # 判断 object 是否为 type 类型
    issubclass(type('child'), type('super'))  # 判断 type_1 是否为 type_2 的子类

    dir(  # 返回当前本地作用域中的名称列表
        object)  # 返回 object 的属性和方法列表

    hasattr(object, str('attr or method'))  # 判断 object 是否包含属性或方法
    getattr(object, str('attr or method'),  # 访问 object 的属性或方法
            Any('default'))  # 若属性不存在，则返回 Any
    setattr(object, str('attr or method'), Any('value'))  # 设置 object 的属性或方法

    callable(object)  # 判断 object 是否可以作为函数调用

    hash(object)  # 若 object 没有哈希值，引发 TypeError
    '''相同大小的数字变量有相同的哈希值（即使数据类型不同）'''


def input_print():
    input(
        object)  # 将 object 写入标准输出（末尾不带换行符）
    print(object, ...,
          sep=str,  # 多个 object 以 sep 分隔（默认为空格）
          end=str)  # 在 object 打印结束后，打印 end（默认为回车）


def run():
    exec(str('statement'),  # 执行字符串形式的语句，没有返回值
         dict('scope_global'),  # 全局命名空间，放置语句中的变量
         dict('scope_local'))  # 局部命名空间
    eval(str('expression'),  # 执行字符串形式的表达式，有返回值
         dict('scope_global'),
         dict('scope_local'))
