import string


def const():
    string.digits  # 数字 0～9
    string.ascii_letters  # 所有 ASCII 字符
    string.ascii_lowercase  # 小写 ASCII 字符
    string.ascii_uppercase  # 大写 ASCII 字符
    string.printable  # 可打印的 ASCII 字符
    string.punctuation  # ASCII 标点字符


def title():
    string.capwords(str,  # 首字母大写
                    sep=str)  # 使用 sep 识别单词（默认为空白字符）
