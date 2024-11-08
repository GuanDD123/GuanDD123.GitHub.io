from io import TextIOWrapper
from _typeshed import FileDescriptorOrPath
from typing import Iterable


def open_close(F: TextIOWrapper):
    open(file=FileDescriptorOrPath,
         mode='w' | ...,
         encoding='utf-8' | ...,
         errors='ignore' | ...,
         buffering=1 | ...,
         newline='')
    F.close()
    '''mode 参数：
     r：只读方式
     rb：二进制只读方式
     r+：读写方式
     rb+：二进制读写方式
     w：写入方式
     wb：二进制写入方式
     w+：读写方式
     wb+：二进制读写方式
     a：追加方式
     ab：二进制追加方式
     a+：读追加方式
     ab+：二进制读追加方式
     '''
    '''errors 参数：
     ignore：忽略错误
     replace：将替换标记（如 '?' ）插入有错误数据的地方
     surrogateescape：把任何不正确的字节表示为 U+DC80 至 U+DCFF 范围内的下方替代码位。当在写入数据时使用 surrogateescape 错误处理器时这些替代码位会被转回到相同的字节（适用于处理具有未知编码格式的文件）
     xmlcharrefreplace：编码格式不支持的字符将被替换为相应的 XML 字符引用 &#nnn;（写入文件时支持）
     backslashreplace：用 Python 的反向转义序列替换格式错误的数据
     namereplace：用 \\N{...} 转义序列替换不支持的字符（编写时支持）
     '''
    '''buffering 参数：
     0：I/O 操作无缓冲，直接将数据写到硬盘上
     1：I/O 操作有缓冲，数据先写到内存里，只有使用 flush 函数或者 close 函数才会将数据更新到硬盘
     大于 1 的数字：代表缓冲区的大小（单位是字节）
     -1（或任何负数）：代表使用默认缓冲区的大小
     '''


def operate(F: TextIOWrapper):
    F.read()
    F.readline()
    F.readlines()

    F.write(str)
    F.writelines(Iterable[str])
