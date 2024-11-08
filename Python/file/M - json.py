import json
from _typeshed import SupportsRead, SupportsWrite
from typing import Any


def operate_str():
    json.loads(s=str[list | dict])
    json.dumps(obj=list | dict,
               ensure_ascii=False,  # 将非 ASCII 字符原样输出
               indent=4)  # 每层缩进设置为 indent 个空格


def operate_file():
    json.load(fp=SupportsRead[str])
    json.dump(obj=Any, fp=SupportsWrite[str],
              ensure_ascii=False,
              indent=4,
              default=lambda x: str(x))  # 值格式错误时，使用自定义函数返回值
