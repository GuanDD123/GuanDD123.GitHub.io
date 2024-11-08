function click() {
    onclick //当用户单击 HTML 元素时触发
    ondblclick //当用户双击对象时触发
}

function mouse() {
    onmousedown //当用户用任何鼠标按钮单击对象时触发
    onmouseup //当用户在对象之上释放鼠标按钮时触发

    onmousemove //当用户将鼠标划过对象时触发
    onmouseover //当用户在一个 HTML 元素上移动鼠标
    onmouseout //当用户从一个 HTML 元素上移开鼠标

    onmousewheel //当鼠标滚轮按钮旋转时触发
}

function keyboard() {
    onkeydown //当用户按下键盘按键时触发
    onkeyup //当用户释放键盘按键时触发

    onhelp //当用户在按 F1 键时触发
}

function object_move() {
    onmove //当对象移动时触发
    onmovestart //当对象开始移动时触发
    onmoveend //当对象停止移动时触发

    ondragend //当用户拖曳操作结束后释放鼠标时触发
}

function other() {
    onload //当某个页面或图像被完成加载
    onstop //当用户单击停止按钮或离开页面时触发

    onfocusin //当元素将要被设置为焦点之前触发
    onblur //当元素失去焦点

    onselect //当文本被选定
    onactivate //当对象设置为活动元素时触发
    onreadystatechange //当在对象上发生对象属性更改时触发

    onchange //当 HTML 元素改变时触发
}