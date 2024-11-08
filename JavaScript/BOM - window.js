/**window 对象：表示浏览器当前打开的窗口*/
function window() {
    window.closed; //返回窗口是否被关闭
    window.defaultStatus; //设置或返回窗口状态栏中的默认文本

    window.length; //设置或返回窗口中的框架数量
    window.name; //设置或返回窗口的名称
    window.opener; //返回对创建此窗口的窗口的引用

    window.innerheight; //返回窗口的文档显示区的高度
    window.innerwidth; //返回窗口的文档显示区的宽度
    window.outerheight; //返回窗口的外部高度
    window.outerwidth; //返回窗口的外部宽度

    window.parent; //返回父窗口
    window.self; //返回对当前窗口的引用，等价于window 属性
    window.top; //返回最顶层的先辈窗口
    window.window; //等价于self 属性，它包含了对窗口自身的引用

    window.screenLeft, window.screenTop, window.screenX, window.screenY; //声明窗口左上角在屏幕上的 x 坐标和 y 坐标

    window.scrollBy(); //按照指定的像素值来滚动内容
    window.scrollTo(); //把内容滚动到指定的坐标
    window.moveBy(); //基于当前窗口的坐标，向某个方向移动指定像素距离
    window.moveTo(); //把窗口的左上角移动到一个指定的坐标

    window.setInterval(); //定时器
    window.setTimeout(); //延时器
    window.clearInterval(); //取消由setInterval() 设置的timeout
    window.clearTimeout(); //取消由setTimeout() 方法设置的timeout

    window.createPopup(); //创建一个弹出窗口
    window.alert(); //显示带有一段消息和一个确认按钮的警告框
    window.prompt(); //显示可提示用户输入的对话框
    window.confirm(); //显示带有一段消息以及确认按钮、取消按钮的对话框

    window.open(); //打开新页面
    window.close(); //关闭页面

    window.focus(); //把键盘的焦点给予窗口
    window.print(); //打印当前窗口的内容

    window.resizeBy(); //按照指定的像素调整窗口的大小
    window.resizeTo(); //把窗口的大小调整到指定的宽度和高度

    window.setInterval(); //按照指定的周期（以毫秒计算）调用函数或计算表达式
    window.setTimeout(); //在指定的毫秒数后调用函数或计算表达式
}

/**document 对象：载入浏览器的 HTML 文档 */
function document() {
    document.body; //<body＞元素
    document.cookie; //当前cookie
    document.lastModified; //文档最后修改日期和时间
    document.referrer; //返回用户在当前页面之前查看的页面的 URL，通常，该页面带有一个指向当前页面的链接（不能更改这个属性的值）
    //如果直接访问给定的 URL，那么将是空白
    document.images; //文档中使用的图像集合
    document.title; //文档标题
    document.URL; //当前 URL（不能更改这个属性的值）
    document.links;
    document.links.length;

    document.getElementById(); //返回指定 id 的引用对象
    document.getElementsByName(); //返回指定名称的对象集合
    document.getElementsByTagName(); //返回指定标签名的对象集合

    document.createTextNode(); // 创建包含指定文本的新文本节点
    document.createElement(); // 为指定的标签创建一个新的 HTML 元素（可以通过更改元素的子对象或者 innerHTML 属性，指定元素中的内容）

    document.open(); //打开流接收输入输出
    document.write(); //显示文本
    document.writeln(); //显示文本（需要在末尾包括一个换行符 (\n)）
}

/** navigator 对象：包含浏览器的有关信息
 * navigator 对象的返回值可以被改变
 */
function navigator() {
    navigator.userAgent; //返回由客户机发送服务器的User-Agent头部的值

    navigator.AppCodeName; //浏览器代码名
    navigator.AppName; //返回浏览器的名称
    navigator.AppVersion; //返回浏览器的平台和版本信息
    navigator.appMinorVersion; //返回浏览器的次级版本信息
    navigator.browserLanguage; //浏览器语言
    navigator.systemLanguage; //返回操作系统使用的默认语言
    navigator.userLanguage; //返回操作系统的自然语言设置

    navigator.cookieEnabled; //指明是否启用 cookie 的布尔值
    navigator.cpuClass; //浏览器系统的 cpu 等级
    navigator.onLine; //是否处于脱机模式
    navigator.webdriver; //返回指明浏览器是否被WebDriver驱动的布尔值
    navigator.hardwareConcurrency; //返回CPU核心数量
    navigator.connection; //网络信息

    navigator.taintEnabled(); //是否启用数据污点
}

/**location 对象：包含有关当前 URL 的信息 */
function location() {
    location.host; //设置或返回主机名和当前URL的端口号
    location.hostname; //设置或返回当前URL的主机名

    location.hash; //设置或返回从井号（# ）开始的URL（锚）
    location.href; //设置或返回完整的URL
    location.port; //设置或返回当前URL的端口号
    location.protocol; //设置或返回当前URL的协议
    location.pathname; //设置或返回当前URL的路径部分
    location.search; //设置或返回从问号（? ）开始的URL（查询部分）

    location.assign(); //加载新文档
    location.reload(); //重新加载文档（如果包括 true 参数，将忽略浏览器的缓存，并且强制进行重新加载，而不管文档是否被更改）
    location.replace(); //替换当前文档（不会影响浏览器的历史记录，即不能使用“后退”按钮转到前一个位置）
}

/**screen 对象：存放有关显示浏览器屏幕的信息 */
function screen() {
    screen.availHeight; //返回屏幕高度（不包括Windows任务栏）
    screen.availWidth; //返回屏幕宽度（不包括Windows任务栏）

    screen.height; //返回显示屏高度
    screen.width; //返回显示屏宽度
    screen.pixelDepth; //返回显示屏幕的颜色分辨率
    screen.updateInterval; //设置或返回屏幕的刷新率
    screen.deviceXDPI; //返回显示屏每英寸水平点数
    screen.deviceYDPI; //返回显示屏每英寸垂直点数
    screen.logicalXDPI; //返回显示屏幕每英寸的水平方向的常规点数
    screen.logicalYDPI; //返回显示屏幕每英寸的垂直方向的常规点数

    screen.bufferDepth; //设置或返回调色板比特深度
    screen.colorDepth; //返回目标设备或缓冲器上调色板的比特深度
    screen.fontSmoothingEnabled; //返回是否启用字体平滑
}

/**history 对象：包含用户在浏览器窗口中访问过的 URL*/
function history() {
    history.length; //浏览器历史列表中的 URL 数量

    history.back(); //加载前一个URL
    history.forward(); //加载下一个URL

    history.go(); //加载某个具体页面
}
