
## 1. 段落

I really like using Markdown.

I think I'll use it to format all of my documents from now on.

## 2. 换行

This is the first line.  （末尾两个空格）
And this is the second line.

## 3. 强调

* 为兼容考虑，在单词或短语中间部分强调时，建议使用星号（asterisks），不使用下划线（underscores）。
  * Markdown 应用程序在如何处理单词或短语中间的下划线上并不一致。

- 粗体 (Bold)
  **Bold text**
- 斜体 (Italic)
  *Italic text*
- 粗体和斜体：
  ***Bold and Italic text***

## 4. 上下标

* A^上标^
* A~下标~

## 5. 删除线

~~世界是平坦的。~~ 我们现在知道世界是圆的。

## 6. 引用

- 块引用
  > Dorothy followed her through many of the beautiful rooms in her castle.
- 多个段落的块引用
  > Dorothy followed her through many of the beautiful rooms in her castle.
  >
  > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
- 嵌套块引用
  > Dorothy followed her through many of the beautiful rooms in her castle.
  >
  > > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

## 7. 列表

### 7.1. 有序列表

1. First item
2. Second item
3. Third item
4. Fourth item

### 7.2. 无序列表

- First item
- Second item
- Third item
- Fourth item

* First item
* Second item
* Third item
* Fourth item

+ First item
+ Second item
+ Third item
+ Fourth item

### 7.3. 任务列表

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

## 8. 定义列表

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

## 9. 代码

- 基本语法
    At the command prompt, type `nano`.
- 转义反引号
    ``Use `code` in your Markdown file.``
- 围栏代码块
  ```markdown
  围栏代码块
  ```

## 10. 分隔线

---

## 11. 链接

### 11.1. 普通链接

[超链接显示名](超链接地址 "超链接title")

### 11.2. 引用链接

引用样式链接是一种特殊的链接，它使 URL 在 Markdown 中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。

- 第一部分
  - 使用两组括号进行格式设置。第一组方括号包围应显示为链接的文本。第二组括号显示了一个标签，该标签用于指向您存储在文档其他位置的链接。
  - 第一组和第二组括号之间空格可以省略
  - 第二组括号中的标签不区分大小写，可以包含字母，数字，空格或标点符号。
    [hobbit-hole] [1]
- 第二部分
  - 放在括号中的标签，其后紧跟一个冒号和至少一个空格（例如[label]:）。
  - 链接的URL，可以选择将其括在尖括号中。
  - 链接的可选标题，可以将其括在双引号，单引号或括号中。
    [1]: 网址
    [1]: 网址 "标题"
    [1]: 网址 '标题'
    [1]: 网址 (标题)
    [1]: <网址> "标题"
    [1]: <网址> '标题'
    [1]: <网址> (标题)

可以将链接的第二部分放在Markdown文档中的任何位置。有些人将它们放在出现的段落之后，有些人则将它们放在文档的末尾（例如尾注或脚注）。

## 12. 图片

### 12.1. md

![图片alt](图片链接 "图片title")(超链接地址)

### 12.2. html (`<img src=...>`)

- <img src="图片链接" alt="图片alt" title="图片title" width=300>

## 13. 脚注

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.
[^bignote]: Here's one with multiple paragraphs and code.
    Indent paragraphs to include them in the footnote.
    `{ my code }`
    Add as many paragraphs as you like.

## 14. 表格

| Syntax    | Description | Test Text   |
|:--------- |:-----------:| -----------:|
| Header    | Title       | Here's this |
| Paragraph | Text        | And more    |

## 15. 转义字符

### 15.1. 可转义的字符

| Character | Name                                           |
| --------- | ---------------------------------------------- |
| \\        | backslash                                      |
| `         | backtick (see also escaping backticks in code) |
| *         | asterisk                                       |
| _         | underscore                                     |
| { }       | curly braces                                   |
| [ ]       | brackets                                       |
| ( )       | parentheses                                    |
| #         | pound sign                                     |
| +         | plus sign                                      |
| -         | minus sign (hyphen)                            |
| .         | dot                                            |
| !         | exclamation mark                               |
| \|        | pipe (see also escaping pipe in tables)        |

### 15.2. 特殊字符自动转义

- HTML 文件中，有两个字符需要特殊处理：< 和 &
  - “<”符号用于起始标签，“&”符号用于标记 HTML 实体
  - 如果只是想要使用这些符号，必须要使用实体的形式，像是“\&lt;”和“\&amp;”

* md 中，如果使用“&”符号的作为 HTML 实体的一部分，那么它不会被转换，而在其它情况下，它则会被转换成“\&amp;”
* md 中，如果使用“<”符号作为 HTML 标签的分隔符，那它不会被转换

## 16. 内嵌HTML标签

- 行级内联标签：如`<span>`、`<cite>`、`<del>`等不受限制，可以在 Markdown 的段落、列表或是标题里任意使用
- 区块标签：如`<div>`、`<table>`、`<pre>`、`<p>`等标签
  - 必须在前后加上空行，以便于内容区分
  - 这些元素的开始与结尾标签，不可以用tab或空白缩进
  - Markdown会自动识别这区块元素，避免在区块标签前后加上没有必要的`<p>`标签
  - Markdown 语法在HTML区块标签中将不会被进行处理

## 17. 网址

- Markdown 官方教程：<https://markdown.com.cn>
