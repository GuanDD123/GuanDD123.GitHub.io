## 1. 文档声明

\<!DOCTYPE html>：将文档标识为 HTML5

\<meta charset="UTF-8">：声明编码格式
\<meta name="viewport" content="width=device-width, initial-scale=1.0">：页面根据设备宽度进行缩放

## 2. 页面标识

```html
<html>
    标识 Web 页面的开始与结束
</html>
```

```html
<head>
    以某种方式描述页面
</head>
```

```html
<title>页面标题</title>
```

```html
<body>
    页面正文
</body>
```

## 3. 注释

```html
<!--注释-->
```

## 4. 区域

```html
<div>常用于组合块级元素</div>
```

```html
<article>一段独立的内容，如新闻文章</article>
```

```html
<section>主题上类似的内容，如一本书的某一章</section>
```

## 5. 介绍性信息、额外信息

```html
<header>介绍性信息</header>
```

```html
<footer>关于其包含元素的额外信息，如版权信息等</footer>
```

## 6. 导航

```html
<nav>导航元素</nav>
```

## 7. 辅助信息

```html
<aside>关于其包含元素的辅助信息</aside>
```

如果位于 \<section> 或 \<article> 内，关系将是那些容器，否则将是整个页面或站点本身。

## 8. 地址信息

```html
<address>与其最近的`<article>`或`<body>`相关的地址信息</address>
```

通常包含在 \<footer> 内

## 9. 标题、段落、换行

```html
<h1>1级标题</h1>
<h2>2级标题</h2>
<h3>3级标题</h3>
<h4>4级标题</h4>
<h5>5级标题</h5>
<h6>6级标题</h6>
```

```html
<p>段落</p>
```

```html
<br />：换行
```

## 10. 文本格式

```html
A<sup>上标</sup>

A<sub>下标</sub>
```

```html
<small>小号文本</small>

<big>大号文本</big>
```

```html
<tt>打印机字体</tt>
```

```html
<pre>等宽文本，保留空格和换行符</pre>
```

## 11. 删除线、下划线

```html
<del>删除线</del>

<s>删除线</s>
```

```html
<u>下划线</u>

<ins>下划线</ins>
```

## 12. 引用

```html
<q>短的引用</q>
```

```html
<cite>引用</cite>
```

```html
<blockquote>块引用</blockquote>
```

## 13. 列表

```html
<ol>
    <li>有序列表</li>
    <li>有序列表</li>
</ol>
```

```html
<ul>
    <li>无序列表</li>
    <li>无序列表</li>
</ul>
```

```html
<dl>
    <dt>概念</dt>
    <dd>定义列表</dd>
</dl>
```

## 14. 代码

```html
<code>代码</code>
```

## 15. 水平分隔线

```html
<hr />
```

## 16. 链接

```html
<a href="地址">链接到某个文件</a>
```

```html
<a href="#id_name">链接到页面中使用id属性标识的某个区域</a>

<a id="id_name"></a>：将页面中某个区域标记为锚。
```

\<a> 给页面上出现标签的特定位置提供了一个名称。
标识区域时，必须使用 \</a>标签，且必须给 id 属性分配一个唯一的名称。

如果链接到页面内不存在的锚或拼写错了锚名称，链接将转到页面顶部。

### 16.1. 发送邮件

```html
<a href="mailto:email_address">点击链接发送邮件</a>

<a
    href="mailto:email_address
    ?subject:默认主题&body=默认正文"
>
    设置默认主题和正文
</a>
```

### 16.2. 在新窗口打开链接

```html
<a href="" target="_blank">链接</a>
```

### 16.3. 伪类 pseudoclass

每个伪类都必须有与之关联的特定颜色。

a:link：未被访问的链接
a:visited：被访问过且存在于浏览器记忆中的链接
a:hover：用户的鼠标悬停于其上的链接
a:active：正在被单击但是尚未释放鼠标的链接

## 17. 图片

```html
<img
    src="地址"
    alt="alt"
    title="title"
    width=""
    height=""
    border=""
    usemap="#map_name"
/>

<map name="map_name">
    <area shape="" coords="" alt="" href="" />
</map>
```

## 18. 多媒体

### 18.1. 使用 HTML5 固有元素播放

```html
<audio src="" preload="" controls autoplay loop></audio>

<video src="" preload="" width="" height="" controls autoplay loop></video>
```

preload：是否缓冲文件或文件元数据（none、auto、metadata）
controls：显示用于音频播放器的控件
autoplay：一加载完文件就播放
loop：重复播放

### 18.2. 使用外部插件播放

```html
<object width="" height="" type="" data=""></object>
```

**音视频格式的 MIME 类型 (MIME type)：**
WAV：audio/vnd.wave
MP3：audio/mpeg
MP4：audio/mp4
WMV：video/x-ms-wmv
MPEG：video/mpeg
MPEG4：video/mp4
QuickTime：video/quicktime

## 19. 表格

```html
<table>
    <caption>
        Title
    </caption>
    <tr>
        <th colspan="2">表头</th>
        <th>表头</th>
    </tr>
    <tr>
        <td rowspan="2">单元格</td>
        <td>单元格</td>
        <td>单元格</td>
    </tr>
    <tr>
        <td>单元格</td>
        <td>单元格</td>
    </tr>
</table>
```

**\<caption> 中 align 属性**
top：标题放在表格的上部
bottom：标题放在表格的下部
left：标题放在表格的左部
right：标题放在表格的右部

**\<td> 和 \<th> 中属性**

rowspan：设置单元格所占行数
colspan：设置单元格所占列数
