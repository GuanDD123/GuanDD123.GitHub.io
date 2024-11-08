import csv
from _typeshed import SupportsWrite
from typing import Iterable, Any


def read():
    f_reader = csv.reader(csvfile=Iterable[str])
    next(f_reader)


def write_list():
    f_writer = csv.writer(csvfile=SupportsWrite[str])
    f_writer.writerow(row=Iterable)
    f_writer.writerows(rows=Iterable[Iterable])


def write_dict():
    from csv import DictWriter
    f_writer = DictWriter(f=SupportsWrite[str], fieldnames=list[str])  # list 参数指定字典中要传给 writerow() 方法并写入文件的值的顺序

    f_writer.writeheader()  # 将构造 DictWriter 对象时指定的 list 参数写入 DictWriter 对象
    f_writer.writerow(rowdict=dict[str, Any])
    f_writer.writerows(rowdicts=Iterable[dict[str, Any]])
