## 1. 在 HTML 中使用 JavaScript

<script type="text/javascript">将文本视作脚本;</script>

<script type="text/javascript" src=""></script>：使用 js 文件中的脚本

## 2. 脚本出现的位置

页面主体内：浏览器加载页面时，把脚本的输出显示为 HTML 文档的一部分

页面头部的`<head>`标签内：通常用于函数

HTML 标签内（事件处理程序 event handler）：使用脚本处理 HTML 元素（无需使用`<script>`标签）

单独的文件中：脚本可以具有任何文件扩展名，或没有扩展名

## 3. 事件

行内绑定：将触发事件直接写到元素标签中
```html
<div onclick="xxx()">点击</div>
```
动态绑定：先获取到 dom 元素，然后在元素上绑定事件
```html
<script>
    var xx=document.getElementById();
    xx.onclick = function(){ }
</script>
```
事件监听：通过 addEventListener() 方法实现
```html
<script>
    var xx=document.getElementById();
    xx.addEventListener('click', function(){ })
</script>
```

## 4. 基本的节点属性

style：节点的样式表值

nodeName：节点的名称（而不是 ID）（这是一个只读的值）
对于基于 HTML 标签的节点，比如`<p>`，名称就是标签名称：p
对于文档节点，名称是特殊的代码：#document
文本节点具有名称#text

nodeType：一个描述节点类型的整数（这是一个只读的值）
1 用于正常的 HTML 标签
3 用于文本节点
9 用于文档节点

nodeValue：文本节点内包含的实际文本（对于其他类型的节点，返回 null）

innerHTML：任何节点的 HTML 内容
可以给这个属性赋予一个值（包括 HTML 标签），并且动态地为节点更改 DOM 子对象

## 5. 节点的关系属性（只读）

firstChild：节点的第一个子对象
lastChild：节点的最后一个子对象

childNodes：包括节点的所有子节点的数组
可以对这个数组使用循环语句，处理给定节点下的所有节点

previousSibling：当前节点之前的兄弟节点（位于同一层级的节点）
nextSibling：当前节点之后的兄弟节点

## 6. 节点方法

appendChild(new)：把指定的新节点追加到对象的所有现有的节点之后
insertBefore(new, old)：把指定的新子节点插入在指定的旧子节点之前，其中后者必须已经存在

replaceChild(new, old)：利用新节点替换指定的旧子节点

removeChild(node)：从对象的子节点集合中移除一个子节点

hasChildNodes()：判断对象是否具有子节点，返回 true/false

cloneNode()：创建现有节点的一个副本（如果提供了参数 true，则副本也会包括原始节点的任何子节点）
