import re


def NOTE():
    '''flags参数：
    re.I：使匹配对大小写不敏感
    re.M：多行匹配，影响^和$
    re.S：使匹配内容包括换行符在内的所有字符
    '''


def _():
    re.compile(pattern=r'',
               flags=re.S | ...)


def replace_elem():
    from re import Pattern
    re.sub(pattern=r'' | Pattern, repl=str, string=str,
           flags=re.S | ...)


def match_elem():
    from re import Pattern

    re.match(pattern=r'' | Pattern, string=str,  # 从字符串的起始位置开始匹配
             flags=re.S | ...)
    re.search(pattern=r'' | Pattern, string=str,
              flags=re.S | ...)

    re.findall(pattern=r'' | Pattern, string=str,
               flags=re.S | ...)
    re.finditer(pattern=r'' | Pattern, string=str,
                flags=re.S | ...)


def match_results(match: re.Match[str]):
    match.group(
        int)  # 返回第 int 个被 () 包围的匹配结果

    match.span()  # 返回匹配的索引范围
    match.start()  # 返回匹配的起始索引
    match.end()  # 返回匹配的末尾索引
