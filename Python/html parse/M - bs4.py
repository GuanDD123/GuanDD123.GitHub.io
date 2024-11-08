import bs4
from bs4 import BeautifulSoup
from _typeshed import SupportsRead


def NOTE():
    '''bs 库有 4 种对象
    BeautifulSoup 对象
    标签 Tag 对象：BeautifulSoup 对象通过 find 和 find_all，或直接调用子标签获取的一列或单个对象
    NavigableString 对象：表示标签里的文字，而不是标签本身
    Comment 对象：用来查找 HTML 文档的注释标签
    '''


def _():
    BeautifulSoup(markup=str | SupportsRead[str], features='html.parser' | ...,  # 对于不标准的 HTML 字符串，可以自动更正格式
                  from_encoding='utf-8')
    '''HTML 解析器比较：
        html.parser：内置标准库
        lxml：速度快、容错能力强。（需要安装 C 语言库）
        xml：速度快、支持 XML 解析。（需要安装 C 语言库）
        html5lib：容错能力最强。（速度慢）
    '''


def get_info(bs: BeautifulSoup, tag: bs4.Tag):
    bs.prettify  # 以标准的缩进格式返回

    tag.get_text()
    tag.text
    tag.string

    tag.name
    tag.attrs
    tag.attrs['attr'] == tag['attr']


def find_tag_direct(bs: BeautifulSoup):
    bs.html.body.h1 == bs.html.h1 == bs.body.h1 == bs.h1

    '''
    调用 BeautifulSoup 对象里的标签时，
    如果这个标签不存在，BeautifulSoup 会返回 None 对象；
    如果再调用这个 None 对象下面的子标签，就会发生 AttributeError 错误。
    '''


def find_tag_from_attr(bs: BeautifulSoup, tag: bs4.Tag):
    bs.find(name=str | list[str],  # 使用 keyword 参数匹配 attr 时可以省略
            attrs=dict(str['attr'], str['value']),
            string=str,  # 匹配标签的文本内容
            recursive=False)  # 只查找子标签
    bs.find_all(name=str | list[str],
                attrs=dict(str['attr'], str['value']),
                string=str,
                recursive=False,
                limit=int)  # 查找前 int 个标签

    tag.find_parent(...)
    tag.find_parents(...)
    tag.find_next_sibling(...)
    tag.find_next_siblings(...)
    tag.find_previous_sibling(...)
    tag.find_previous_siblings(...)

    tag.find_next(...)
    tag.find_all_next(...)
    tag.find_previous(...)
    tag.find_all_previous(...)


def find_tag_from_location(tag: bs4.Tag):
    tag.contents  # 返回由所有直接子标签组成的列表
    tag.children
    tag.descendants

    tag.parent
    tag.parents

    tag.next_sibling
    tag.next_siblings
    tag.previous_sibling
    tag.previous_siblings


def find_tag_from_css(bs: BeautifulSoup):
    bs.select_one(selector=str)
    bs.select(selector=str,
              limit=int)
