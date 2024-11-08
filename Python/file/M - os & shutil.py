import os
import os.path
import shutil
from _typeshed import StrPath, StrOrBytesPath, FileDescriptorOrPath


def file_attrs():
    __file__

    os.getcwd()  # 返回当前活动目录

    os.path.dirname(p=StrPath)
    os.path.basename(p=StrPath)
    os.listdir(path=StrOrBytesPath)

    os.stat(path=FileDescriptorOrPath)  # 返回文件状态
    os.path.getsize(filename=FileDescriptorOrPath)  # 文件不存在或不可访问，引发 OSError 异常


def operate():
    os.makedirs(name=StrOrBytesPath,  # 创建多级目录
                exist_ok=True)  # 若目录存在，不报错
    os.mkdir(path=StrOrBytesPath)  # 创建单级文件夹；文件夹存在，引发 FileExistsError；父目录不存在，引发 FileNotFoundError

    os.rename(src=StrOrBytesPath, dst=StrOrBytesPath)  # 在 Windows 上，若 dst 存在则会引发 FileExistsError

    shutil.copytree(src=StrPath, dst=StrPath,
                    dirs_exist_ok=True)  # 若 dst 存在，不报错
    shutil.copyfile(src=StrOrBytesPath, dst=StrOrBytesPath)
    shutil.copy(src=StrPath, dst=StrPath)

    shutil.move(src=StrPath, dst=StrPath)  # 若 dst 为目录，则 src 在 dst 中不能已存在

    os.remove(path=StrOrBytesPath)  # 删除文件
    os.rmdir(path=StrOrBytesPath)  # 删除空文件夹
    os.removedirs(name=StrOrBytesPath)  # 递归删除空目录
    shutil.rmtree(path=StrOrBytesPath)


def logic_judge():
    os.path.isfile(path=FileDescriptorOrPath)
    os.path.isdir(s=FileDescriptorOrPath)

    os.path.isabs(s=StrOrBytesPath)

    os.path.exists(path=FileDescriptorOrPath)


def split_join():
    os.path.split(p=StrPath)  # 拆分路径，返回 tuple[路径除最后部分外的所有内容，路径最后一部分]
    # 若 path 以斜杠结尾，tail 将为空；若 path 中没有斜杠，head 将为空
    # 若 head 不是根目录，末尾的斜杠会被去掉）
    os.path.splitext(p=StrPath)  # 拆分路径，返回 tuple[路径除拓展名外的所有内容，拓展名]

    os.path.join(StrOrBytesPath, StrOrBytesPath, ...)


def system_attrs():
    os.getenv(key=str,
              default=str)  # key 不存在，则返回 default
    os.putenv(str('name'), str('value'))

    os.linesep  # 返回当前操作系统使用的行终止符
    os.name  # Windows 是 nt，Linux/Unix 是 posix，java 虚拟机是 java
