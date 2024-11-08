from typing import Iterable


bytes()  # 不可变序列
bytearray()  # 可变序列


def _(B: bytes):
    r''  # 不对 ‘\’ 作特殊处理；最后一个字符不能是 ‘\’
    repr(str)  # 返回字符串的 python 表达式表示
    ascii(str)  # 返回字符串的 ASCII 表示

    bytes(int)   # 创建长度为 int 的，以零值填充的 bytes 对象
    bytes(Iterable[int])  # 需 0<=int<256，否则会引发 ValueError
    bytes(str, encoding='utf=8' | ...)

    bytes.fromhex(str[hex])  # 两个十六进制数码对应一个字节
    B.hex(
        sep=str,  # 指定输出的十六进制码中，单个数码之间的分隔符
        bytes_per_sep=int)  # 每输出 int 个数码输出一个分隔符；负数表示从左开始计算，正数表示从右开始


def max_min():
    max(...)
    min(...)

    max(str | bytes,  str | bytes, ...)


def length():
    len(str | bytes)


def logic_judge(S: str, SB: str | bytes):
    SB.isalnum()  # 判断是否所有字符都是字母或数字，且 len(str)>0
    SB.isalpha()  # 判断是否所有字符都是字母，且 len(str)>0
    SB.isspace()  # 判断是否所有字符都是空白字符，且 len(str)>0
    SB.isascii()  # 判断是否所有字符都是 ASCII，或 len(str)=0
    S.isdecimal()  # 判断是否所有字符都是十进制字符，且 len(str)>0
    SB.isdigit()  # 判断是否所有字符都是数字，且 len(str)>0
    S.isnumeric()  # 判断是否所有字符都是数值，且 len(str)>0

    S.isidentifier()  # 判断字符串是否为有效的标识符

    S.isprintable()  # 判断是否所有字符均为可打印字符，或 len(str)=0


def format_(V: str):
    f'...{V}...' == '...{}...'.format(V)
    '''格式化参数（var:S=<+#N,.Nf）
    S：使用 S 填充空白（需要与 = 或 </^/> 同时使用）
    =：将填充字符 S 放在符号和数字之间（不能与 </^/> 同时使用）
    <、^、>：左对齐、居中、右对齐
    -、+、(空格)：正数前什么也不加、加上 +、加上空格
    #：二/八/十六进制数加前缀、g 格式保留小数点
    N：最少占 N 个字符空间
    ,：添加千位分隔符
    .N：指定小数位数

    s：保持字符串的格式不变（字符串默认使用的说明符）
    d：将整数视为十进制数进行处理（整数默认使用的说明符）
    b：将整数表示为二进制数
    o：将整数表示为八进制数
    x：将整数表示为十六进制数并使用小写字母
    X：与 x  相同，但使用大写字母
    c：将整数解读为Unicode码点
    g：自动在定点表示法和科学表示法之间做出选择（小数默认使用的说明符，默认至少有 1 位小数）
    G：与 g  相同，但使用大写表示指数和特殊值
    n：与 g  相同，但插入随区域而异的数字分隔符
    f：将小数表示为定点数
    F：与 f  相同，但对于特殊值（nan 和 inf），使用大写表示
    e：使用科学表示法表示小数（用 e 表示指数）
    E：与 e  相同，但使用 E 表示指数
    %：将数表示为百分比值（乘以100，按说明符 f  设置格式，再在后面加上 %）
    '''


def concatenate(SB: str | bytes):
    SB + SB
    SB * int == int * SB

    SB.join(Iterable[str])  # Iterable 存在非字符串值，引发 TypeError（包括 bytes）


def split(SB: str | bytes):
    SB.split()
    SB.rsplit()

    SB.split(
        sep=str,  # 使用 sep 作为分隔符（默认为空白字符）
        maxsplit=int)  # 最多进行 int 次拆分
    SB.splitlines(
        keepends=True)  # 结果列表中包含换行符

    SB.partition(str)  # 在 str 第一次出现的位置拆分
    SB.rpartition(str)
    # 返回 tuple(分隔符之前的部分，分隔符，分隔符之后的部分)；
    # 若未找到分隔符，则返回 tuple(原字符串，''，'')

    SB.removeprefix(str)  # 若 SB 以 str 开头，返回 str 之后的部分；否则，返回 SB 的副本
    SB.removesuffix(str)  # 若 SB 以 str 结尾，返回 str 之前的部分；否则，返回 SB 的副本


def upper_lower(SB: str | bytes):
    SB.title()
    SB.upper()
    SB.lower()
    SB.swapcase()

    SB.istitle()
    SB.isupper()
    SB.islower()


def start_end(SB: str | bytes):
    SB.strip(...)
    SB.lstrip(...)
    SB.rstrip(...)
    SB.strip(
        str)  # 设置要移除的 str（参数值的所有组合）（默认为空白字符）

    SB.center(...)
    SB.ljust(...)
    SB.rjust(...)
    SB.center(int,  # 返回长度为 int 的字符串，str 居中
              str)  # 使用 str 填充（默认为空格）
    SB.zfill(int)  # 返回长度为 int 的字符串，str 靠右，左边填充 ASCII 0

    SB.startswith(...)
    SB.endswith(...)
    SB.startswith(str | tuple[str])
    SB.startswith(str | tuple[str], int('start'),
                  int('stop'))


def select_elem(SB: str | bytes):
    ... in ...
    ... not in ...
    SB in SB

    SB.find(...)
    SB.rfind(...)
    SB.find(str)  # 找不到 str 时，返回 -1
    SB.find(str, int('start'),
            int('stop'))

    SB.index(...)
    SB.rindex(...)
    SB.index(str)  # 找不到 str，引发 ValueError
    SB.index(str, int('start'),
             int('stop'))

    SB.count(str)  # 返回 str 在 SB 中非重叠出现的次数
    SB.count(str, int('start'),
             int('stop'))


def replace_elem(SB: str | bytes, S: str):
    table = str.maketrans(str('old'), str('new'))  # 根据两字符串的映射关系创建转换表
    table = str.maketrans(dict)
    S.translate(table)  # 一个字符替换为一个字符

    SB.replace(str | bytes('old'), str | bytes('new'),
               int)  # 最多替换 int 个子串

    SB.expandtabs(  # 将字符串中的 \t 替换为一个或多个空格，直到当前列等于下一个制表位；若遇到 \n 或 \r，则将当前列数置为 0
        tabsize=int)  # 设置 int 个字符为一个制表位（默认为 8 个字符）


def encode_decode(S: str, B: bytes):
    S.encode(encoding='utf-8' | ...,  # 编码错误会引发 UnicodeError
             errors='ignore' | ...)

    B.decode(encoding='utf-8' | ...,  # 解码错误会引发 UnicodeError
             errors='ignore' | ...)

    '''errors 参数：
    ignore：忽略错误
    replace：用替代标记替换。编码时，使用 ? (ASCII 字符)；解码时，使用 � (U+FFFD，官方的 REPLACEMENT CHARACTER)
    backslashreplace：用反斜杠转义序列替换。编码时，使用格式为 \\xhh \\uxxxx \\Uxxxxxxxx 的 Unicode 码位十六进制表示形式；解码时，使用格式为 \\xhh 的字节值十六进制表示形式
    surrogateescape：解码时，将字节替换为 U+DC80 至 U+DCFF 范围内的单个代理代码；编码时，此代理将被转换回相同的字节（适用于处理具有未知编码格式的文件）
    xmlcharrefreplace：用 XML/HTML 数字字符引用替换（格式为 &#num; 的 Unicode 码位十进制表示形式）
    namereplace：用 \\N{...} 转义序列替换，出现在花括号中的是来自 Unicode 字符数据库的 Name 属性
    '''
