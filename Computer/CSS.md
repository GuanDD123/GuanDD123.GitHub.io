## 1. 在 HTML 中使用 CSS

内部样式表和外部样式表都需要包含在\<head>中。

\<style type="text/css">内部样式表\</style>

内联样式：指通过 style 属性在 \<p>、\<div>、\<span> 内创建并应用样式规则。
\<span>\</span>：除指定应用所添加的任何 style 属性的内容范围外，不做任何其他事情。

外部样式表：\<link type="text/css" rel="stylesheet" href="" />

## 2. 样式类

tag_name.class_name {...}：创建应用于特定标签的样式类
.class_name {...}：创建应用于任何标签的样式类

引用样式类时，可在 class 属性中指定类名称。

## 3. 样式 ID

tag_name#id_name {...}：创建应用于特定标签的样式 ID
#id_name {...}：创建应用于任何标签的样式 ID

引用样式 ID 时，可在 id 属性中指定 ID 名称。

## 4. 相对定位 display 属性值

block：在新行上显示元素
list-item：在新行上显示元素，并在其旁边带有一个列表项标记

inline：利用当前段落内联显示元素

none：不显示元素

## 5. width 和 height 属性值

in：英寸

cm：厘米
mm：毫米

%：百分比

px：像素

pt：磅

## 6. 边框 border

border（border-left、border-right、border-top、border-bottom）
border-width
border-style
border-color

border-collapse:collapse：合并表格中相邻的边框

border-spacing：表格边框的水平和垂直间距

### 6.1. border-style 属性值

solid：单线边框
double：双线边框

dashed：短划虚线边框
dotted：点线边框

groove：具有沟槽外观的边框
ridge：具有脊状外观的边框
inset：具有内嵌外观的边框
outset：具有外凸外观的边框

none：无边框
hidden：实际上等同于 none

## 7. 分栏

-column-count：指定应分为的列数
-webkit-column-count：Safari and Chrome
-moz-column-count：Firefox

-column-gap：指定列之间的空隙
-webkit-column-gap：Safari and Chrome
-moz-column-gap：Firefox

-column-span：指定某个元素应该跨越多少列
-webkit-column-span：Safari and Chrome

## 8. 边距 margin、填充 padding

1个值：设置四个方向
2个值：分别设置上下、左右
3个值：分别设置上、左右、下
4个值：分别设置四个方向

margin（margin-top、margin-right、margin-bottom、margin-left）

padding（padding-top、padding-right、padding-bottom、padding-left）

## 9. 文本属性

text-align：水平对齐（left、center、right）
vertical-align：垂直对齐（top、text-top、middle、bottom、text-bottom、baseline）

line-height：行高（通常以磅为单位）

text-indent：缩进

letter-spacing：字间距（具体的数值；inherit (从父元素继承) ）

## 10. 浮动 float 属性值

left、right：将图像对齐到左/右边，并使文本环绕在另一边

## 11. 字体

font-family
font-size
font-style：（normal、italic）
font-weight：（lighter、normal、bold、bolder；数值 (400=normal、700=bold)）

## 12. 颜色

color：文本颜色
background-color：背景色

**颜色定义方式：**
颜色名称，如 green
十六进制，如#ff6600
简写方式，如#f60
RGB 方式，如 rgb(255, 255, 255)，取值范围为 0 ～ 255
RGBA 方式，如 rgba(255, 255, 255, 1)，‘A’表示 Alpha 的（色彩空间）透明度

## 13. 背景

background-image:url(链接)：背景图

background-repeat：背景是否在水平和垂直方向上重复（repeat-x、repeat-y、no-repeat）

background-position：背景位置（top-left、top-center、top-right、center-left、center-center、center-right、bottom-left、bottom-center、bottom-right；像素和百分比位置）

## 14. 列表样式

list-style-image：放置一幅图像作为列表项标记（url(链接)、inherit）

list-style-position：列表项中标记的位置（inside、inherit）

list-style-type：列表项标记本身的类型

### 14.1. list-style-type 属性值

none：隐藏项目符号

disc：实心圆点
circle：空心圆
square：实心正方形

decimal：数字
decimal-leading-zero：0 开头的数字
upper-roman：大写罗马数字
lower-roman：小写罗马数字
upper-alpha：大写字母
lower-alpha：小写字母

## 15. 链接的下划线 text-decoration 属性值

none：隐藏链接的下划线

## 16. 媒体查询

max-width: 1200px - 大型桌面设备
max-width: 992px - 中型设备（平板）
max-width: 768px - 小型设备（手机）
max-width: 576px - 超小屏设备

@media (max-width: 768px) {}
