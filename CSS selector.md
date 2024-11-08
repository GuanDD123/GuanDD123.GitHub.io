**.str[class]**：选择 class="class" 的所有元素
**#str[id]**：选择 id="id" 的所有元素
**\***：选择所有元素

**str[element]**：选择所有 \<element> 元素
**str[element_1], str[element_2]**：选择所有 \<element_1> 元素和所有 \<element_2> 元素
**str[element_1] str[element_2]**：选择 \<element_1> 元素内部的所有 \<element_2> 元素
**str[element_1] > str[element_2]**：选择父元素为 \<element_1> 的所有 \<element_2> 元素
**str[element_1] + str[element_2]**：选择紧接在 \<element_1> 元素之后的所有 \<element_2> 元素

**[str[attribute]]**：选择带有 attribute 属性的所有元素
**[str[attribute] = str[value]]**：选择 attribute="value" 的所有元素
**[str[attribute] ~= str[value]]**：选择 attribute 属性包含单词 value 的所有元素
**[str[attribute] |= str[value]]**：选择 attribute 属性值以 value 开头的所有元素

**str[a]:link**：选择所有未被访问的链接
**str[a]:visited**：选择所有已被访问的链接
**str[a]:active**：选择活动链接
**str[a]:hover**：选择鼠标指针位于其上的链接

**str[input]:focus**：选择获得焦点的 \<input> 元素
**str[news]:target**：选择当前活动的 #news 元素
**str[input]:enabled**：选择每个启用的 \<input> 元素
**str[input]:disabled**：选择每个禁用的 \<input> 元素
**str[input]:checked**：选择每个被选中的 \<input> 元素

**str[p]:first-letter**：选择每个 \<p> 元素的首字母
**str[p]:first-line**：选择每个 \<p> 元素的首行

**str[p]:first-of-type**：选择属于其父元素的首个 \<p> 元素的每个 \<p> 元素
**str[p]:last-of-type**：选择属于其父元素的最后 \<p> 元素的每个 \<p> 元素
**str[p]:only-of-type**：选择属于其父元素唯一的 \<p> 元素的每个 \<p> 元素
**str[p]:first-child**：选择属于父元素的第一个子元素的每个 \<p> 元素
**str[p]:last-child**：选择子元素中的最后一个 \<p> 元素
**str[p]:only-child**：选择属于其父元素的唯一子元素的每个 \<p> 元素
**str[p]:nth-child(int[n])**：选择属于其父元素的第 n 个子元素的每个 \<p> 元素
**str[p]:nth-last-child(int[n])**：同上，但从最后一个子元素开始计数
**str[p]:nth-of-type(int[n])**：选择属于其父元素第 n 个 \<p> 元素的每个 \<p> 元素
**str[p]:nth-last-of-type(int[n])**：同上，但从最后一个子元素开始计数

**str[p]:before**：在每个 \<p> 元素的内容之前插入内容
**str[p]:after**：在每个 \<p> 元素的内容之后插入内容

**str[p]:lang(str[language])**：选择以 language 开头的 lang 属性值的每个 \<p> 元素
**str[element_1]~str[element_2]**：选择前面有 \<element_1> 元素的每个 \<element_2> 元素

**[str[attribute] ^= str[value]]**：选择其 attribute 属性值以 value 开头的每个 \<a> 元素
**[str[attribute] $= str[value]]**：选择其 attribute 属性以 value 结尾的所有 \<a> 元素
**[str[attribute] _= str[value]]**：选择其 attribute 属性中包含 value 子串的每个 \<a> 元素

**:root**：选择文档的根元素
**str[p]:empty**：选择没有子元素的每个 \<p> 元素（包括文本节点）

**:not(str[selector])**：选择非 \<selector> 元素的每个元素
**::selection**：选择被用户选取的元素部分
