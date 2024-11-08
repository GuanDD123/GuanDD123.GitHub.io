from typing import Iterable, Any


def _():
    14_000_000 == 14000000
    complex(
        real=int | float | complex,
        imag=int | float | complex)


def max_min():
    max(...)
    min(...)

    max(float, float, ...)
    max(Iterable[float],  # 若 Iterable 为空，引发 ValueErr
        default=Any)  # 若 Iterable 为空，返回 default


def basic_operate(IF: int | float, IF_2: int | float):
    sum(Iterable[int | float | complex])
    IF % IF_2 == IF - IF // IF_2 * IF_2
    divmod(int | float('x'), int | float('y')) == (IF // IF_2, IF % IF_2)
    IF ** IF_2
    pow(base=int | float | complex, exp=int | float | complex,
        mod=int)  # 以乘方结果作为被除数，返回余数
    abs(int | float | complex)

    round(number=float,  # 返回四舍五入的整数值，半数值(.5) 会舍入到偶数
          ndigits=int)  # 最多保留 int 位小数


def int_to_bytes(I: int):
    (I).to_bytes(  # int 大于 255、小于 0 时，引发 OverflowError
        length=int,  # 使用 length 个字节表示
        byteorder='little',  # 最高位字节放在末尾
        signed=True)  # 使用 2 的补码表示整数


def base_conversion_int():
    bin(int)
    oct(int)
    hex(int)

    int(str[bin | oct | hex], base=2-36)


def base_conversion_float(F: float):
    F.hex()

    float.fromhex(str[hex])
