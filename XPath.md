## 1. XPath 运算符

or、and、mod、|、+、-、\*、div、 =、!=、<、<=、>、>=

## 2. 获取属性值

/@attr：获取 attr 属性值
/attribute::\* ：获取所有属性值

## 3. 获取节点文本

/text()：获取当前节点的文本
//text()：获取子孙节点的文本

## 4. 根据属性选取节点

/@attr：选择带 attr 属性的所有节点
/node[@*]：选取带任意属性的 node 节点
/node[@attr="attr_value"]：选取 attr 属性值为 attr_value 的 node 节点
/node[contains(@attr, "attr_value")]：选取 attr 属性值包含 attr_value 的 node 节点

## 5. 根据位置选取节点

/_ == /child::\* ：选取所有子结点
//_ == /descendant::\* ：选取所有子孙节点
/following::\*：选取之后的所有节点
/following-sibling::\*：选取之后的所有兄弟节点
/\.\. == /parent::\* ：选取父节点
/ancestor::\* ：选取所有祖先节点

## 6. 从多个匹配节点选取特定次序的节点

/node[int('position')]：选取匹配的第 position 个 node 节点
/node[last()]：选取匹配的最后一个 node 节点
/node[last()-int('num')]：选取匹配的第最后 num+1 个 node 节点
/node[position()<int('position')]：选取匹配的位置小于 position 的 node 节点
