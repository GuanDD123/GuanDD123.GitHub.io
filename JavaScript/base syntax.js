function datatype() {
    String, '...', "...", `...`
    Number // 将数字存储为 64 位浮点数
    Boolean
    null
    undefined
    Symbol //独一无二的值

    Object
    Array
    Function
}


function statement_identifier() {
    do { } while (condition);
    while (condition) { }
    for (expression; condition; expression) { }

    if (condition) { } else { }
    switch (key) { case value: break; default: break; }

    try { } catch (error) { } finally { }// 异常捕获
    Throw //抛出异常

    class name { }
    function name(args) { }

    var variable_name
    const const_variable_name = 'value' //也可声明快作用域变量
    let local_variable_name //声明块作用域的变量

    debugger //断点调试

    this //当前所属对象

    return
}

function math_operator() {
    Number + Number
    Number - Number
    Number * Number
    Number / Number
    Number % Number
    Number++, ++Number
    Number--, --Number
}

function compare_operator() {
    Object == Object
    Object === Object //相等值或者相等类型
    Object != Object
    Object !== Object //不相等值或者不相等类型
    Object > Object
    Object < Object
    Object >= Object
    Object <= Object
}

function condition_operator() {
    (condition) ? 'result_1' : 'result_2'
}

function logic_operator() {
    condition && condition
    condition || condition
    !condition
}

function bit_operator() {
    /*
    执行位运算之前，JavaScript 将数字转换为 32 位有符号整数；
    执行位运算之后，将结果转换为 64 位数。
    */
    Object & Object //如果两位都是1， 则设置每位为1
    Object | Object //如果两位之一为1， 则设置每位为1
    ~Object //反转所有位
    Object ^ Object //异或运算

    Object << Object //零填充左位移
    Object >> Object //有符号右位移
    Object >>> Object //零填充右位移
}